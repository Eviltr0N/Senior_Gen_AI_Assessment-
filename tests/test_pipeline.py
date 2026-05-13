"""
end to end pipeline tests and GCP SDK mock verification.
"""

from unittest.mock import MagicMock

import pytest

from src.pipeline import RAGPipeline
from src.corpus import CORPUS


class TestRAGPipeline:
    """end to end tests for the RAG pipeline orchestrator.
    """

    def test_ingest_default_corpus(self, mock_generative_model):
        pipeline = RAGPipeline()
        count = pipeline.ingest()
        assert count == len(CORPUS)

    def test_ingest_custom_documents(self, mock_generative_model):
        pipeline = RAGPipeline()
        custom_docs = [
            {"id": "custom_1", "text": "Custom document text", "metadata": {"source": "test"}},
            {"id": "custom_2", "text": "Another custom doc", "metadata": {"source": "test"}},
        ]
        count = pipeline.ingest(custom_docs)
        assert count == 2

    def test_search_before_ingest_raises(self, mock_generative_model):
        pipeline = RAGPipeline()
        with pytest.raises(RuntimeError, match="Call ingest"):
            pipeline.search("test query", strategy="a")

    def test_search_invalid_strategy_raises(self, mock_generative_model):
        pipeline = RAGPipeline()
        pipeline.ingest()
        with pytest.raises(ValueError, match="Unknown strategy"):
            pipeline.search("test", strategy="c")

    def test_strategy_a_search(self, mock_generative_model):
        pipeline = RAGPipeline()
        pipeline.ingest()
        results = pipeline.search("load balancing", strategy="a")
        assert isinstance(results, list)
        assert len(results) == 3

    def test_strategy_b_search(self, mock_generative_model):
        pipeline = RAGPipeline()
        pipeline.ingest()
        result = pipeline.search(
            "How does the system handle peak load?", strategy="b"
        )
        assert isinstance(result, dict)
        assert "expanded_query" in result
        assert len(result["results"]) == 3

    def test_full_pipeline_e2e(self, mock_generative_model):
        """Full pipeline: ingest ->> search with both strategies ----> compare."""
        pipeline = RAGPipeline()
        pipeline.ingest()

        query = "How does the system handle peak load?"

        results_a = pipeline.search(query, strategy="a")
        results_b = pipeline.search(query, strategy="b")

        # Both should return results
        assert len(results_a) == 3
        assert len(results_b["results"]) == 3

        # Strategy B should include the expanded query
        assert results_b["expanded_query"] != query


class TestGCPMockVerification:
    """Verify that GCP SDK mocks are correctly wired."""

    def test_text_embedding_model_mock_called(self, mock_vertex_embedding):
        """Verify TextEmbeddingModel.from_pretrained is called correctly."""
        from src.embedding import VertexEmbeddingService

        service = VertexEmbeddingService()
        service.embed(["test"])

        mock_vertex_embedding.from_pretrained.assert_called_once_with("textembedding-gecko")

    def test_text_embedding_model_get_embeddings_called(self, mock_vertex_embedding):

        from src.embedding import VertexEmbeddingService

        service = VertexEmbeddingService()
        texts = ["hello", "world"]
        service.embed(texts)

        mock_instance = mock_vertex_embedding.from_pretrained.return_value
        mock_instance.get_embeddings.assert_called_once_with(texts)

    def test_generative_model_mock_called(self, mock_generative_model):
        """Verify GenerativeModel is  the correct model name."""
        from src.retrieval import QueryExpander

        expander = QueryExpander()
        expander.expand("How does the system handle peak load?")

        mock_generative_model.assert_called_once_with("gemini-3-flash-preview")
        mock_generative_model.return_value.generate_content.assert_called_once()

    def test_mocks_do_not_leak_between_tests(self, mock_generative_model):

        from src.retrieval import QueryExpander

        expander = QueryExpander()
        # First call
        expander.expand("How does the system handle peak load?")
        assert mock_generative_model.return_value.generate_content.call_count == 1

        # Second call in same test
        expander.expand("What security measures protect user data?")
        assert mock_generative_model.return_value.generate_content.call_count == 2
