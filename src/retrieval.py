"""
Retrieval strategies for the RAG pipeline.

strategyA: Raw vector similarity search, direct query embedding.

strategyB: AI enhanced retrieval, query expansion via GenerativeModel then search.

QueryExpander: Uses a (mocked) gemini Model to rewrite queries.
"""

from vertexai.generative_models import GenerativeModel

from src.config import DEFAULT_TOP_K, VERTEX_GENERATIVE_MODEL
from src.storage import ChromaStore


class QueryExpander:
    """
    Expands user queries using a generative model (gemini) for better semantic retrieval (mocked here).

    """
    # System prompt depends on data and use case
    SYSTEM_PROMPT = (
        "You are a search query optimizer for a technical knowledge base about "
        "distributed systems and cloud infrastructure. Rewrite the following user "
        "query to be more specific and include related technical terms that would "
        "improve semantic search results. Return ONLY the rewritten query, nothing else."
    )

    def __init__(self, model_name: str = VERTEX_GENERATIVE_MODEL):
        self.model = GenerativeModel(model_name)

    def expand(self, query: str) -> str:
        prompt = f"{self.SYSTEM_PROMPT}\n\nOriginal query: {query}"
        response = self.model.generate_content(prompt)
        return response.text


def _format_results(raw_results: dict) -> list[dict]:
    """

    Convert ChromaDB raw result dict into a list of result dicts
    """
    formatted = []

    ids = raw_results["ids"][0]
    documents = raw_results["documents"][0]
    distances = raw_results["distances"][0]
    metadatas = raw_results["metadatas"][0]

    for doc_id, text, distance, metadata in zip(ids, documents, distances, metadatas):
        formatted.append(
            {
                "id": doc_id,
                "text": text,
                "distance": round(distance, 4),
                "metadata": metadata,
            }
        )
    return formatted


class StrategyA:
    """
    Strategy A - Raw Vector Search (no expansion).

    """

    def __init__(self, store: ChromaStore):
        self.store = store

    def retrieve(self, query: str, top_k: int = DEFAULT_TOP_K) -> list[dict]:
        """Retrieve top k documents via direct embedding similarity."""
        raw = self.store.query(query, n_results=top_k)
        return _format_results(raw)


class StrategyB:
    """
    StrategyB - AI Enhanced Retrieval (using query expansion).

    """

    def __init__(self, store: ChromaStore, expander: QueryExpander):
        self.store = store
        self.expander = expander

    def retrieve(self, query: str, top_k: int = DEFAULT_TOP_K) -> dict:
        expanded_query = self.expander.expand(query)
        raw = self.store.query(expanded_query, n_results=top_k)
        results = _format_results(raw)
        return {
            "original_query": query,
            "expanded_query": expanded_query,
            "results": results,
        }
