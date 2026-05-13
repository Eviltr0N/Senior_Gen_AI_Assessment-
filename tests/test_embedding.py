"""
Tests for the embedding module

"""

from src.embedding import LocalEmbeddingService


class TestLocalEmbeddingService:
    """
    
    Tests for the local sentence-transformers embedding service.
    """

    def test_embed_returns_list_of_vectors(self):
        service = LocalEmbeddingService()
        vectors = service.embed(["hello world"])
        assert isinstance(vectors, list)
        assert isinstance(vectors[0], list)
        assert len(vectors) == 1

    def test_embed_vector_dimensions(self):
        """all-MiniLM-L6-v2 produces 384-dimensional vectors."""
        service = LocalEmbeddingService()
        vectors = service.embed(["test sentence"])
        assert len(vectors[0]) == 384

    def test_embed_multiple_texts(self):
        service = LocalEmbeddingService()
        texts = ["first sentence", "second sentence", "third sentence"]
        vectors = service.embed(texts)
        assert len(vectors) == 3
        assert all(len(v) == 384 for v in vectors)

    def test_similar_texts_have_close_embeddings(self):
        """
        Semantically similar texts should produce similar vectors.
        """
        service = LocalEmbeddingService()
        vectors = service.embed([
            "the cat sat on the mat",
            "a kitten rested on the rug",
            "quantum computing uses qubits",
        ])
        # Compute cosine similarity manually
        import numpy as np
        def cosine_sim(a, b):
            return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

        sim_related = cosine_sim(vectors[0], vectors[1])
        sim_unrelated = cosine_sim(vectors[0], vectors[2])
        assert sim_related > sim_unrelated


class TestVertexEmbeddingService:
    """]
    mocked Vertex AI embedding service.
    """

    def test_vertex_embed_with_mock(self, mock_vertex_embedding):
        from src.embedding import VertexEmbeddingService

        service = VertexEmbeddingService()
        vectors = service.embed(["test input"])

        assert len(vectors) == 1
        assert len(vectors[0]) == 384
        mock_vertex_embedding.from_pretrained.assert_called_once_with("textembedding-gecko")

    def test_vertex_embed_multiple_texts(self, mock_vertex_embedding):
        from src.embedding import VertexEmbeddingService

        service = VertexEmbeddingService()
        vectors = service.embed(["text one", "text two"])

        assert len(vectors) == 2
        assert all(len(v) == 384 for v in vectors)

    def test_vertex_mock_produces_real_embeddings(self, mock_vertex_embedding):

        from src.embedding import VertexEmbeddingService

        service = VertexEmbeddingService()
        vectors = service.embed(["meaningful text about machine learning"])

        # Real embeddings should not be all zeros
        assert any(v != 0.0 for v in vectors[0])
