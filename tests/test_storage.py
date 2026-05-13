"""
Tests for the ChromaDB storage module.

"""

from src.corpus import CORPUS


class TestChromaStore:
    """
    Tests for the ChromaDB vector store wrapper.
    """

    def test_add_documents(self, chroma_store):
        chroma_store.add_documents(CORPUS[:3])
        assert chroma_store.count == 3

    def test_add_full_corpus(self, chroma_store):
        chroma_store.add_documents(CORPUS)
        assert chroma_store.count == len(CORPUS)

    def test_query_returns_correct_count(self, populated_store):
        results = populated_store.query("load balancing", n_results=3)
        assert len(results["ids"][0]) == 3
        assert len(results["documents"][0]) == 3
        assert len(results["distances"][0]) == 3

    def test_query_returns_relevant_results(self, populated_store):

        results = populated_store.query("load balancing and auto-scaling", n_results=1)
        top_id = results["ids"][0][0]
        assert top_id == "doc_001"

    def test_query_returns_metadata(self, populated_store):
        results = populated_store.query("database replication", n_results=1)
        metadata = results["metadatas"][0][0]
        assert "topic" in metadata

    def test_query_distance_ordering(self, populated_store):
        """Results should be ordered by distance (ascending = most similar first)."""
        results = populated_store.query("caching and CDN performance", n_results=3)
        distances = results["distances"][0]
        assert distances == sorted(distances)

    def test_single_result_query(self, populated_store):
        results = populated_store.query("OAuth JWT authentication", n_results=1)
        assert len(results["ids"][0]) == 1
