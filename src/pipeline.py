"""
RAG Pipeline orchestrator

"""

from src.corpus import CORPUS
from src.retrieval import QueryExpander, StrategyA, StrategyB
from src.storage import ChromaStore


class RAGPipeline:
    """
    main orchestration class that manages data ingestion and provides access to both retrieval strategies.
    the store and expander can be replaced with mocks or alternative implementations for testing.
    """

    def __init__(
        self,
        store: ChromaStore | None = None,
        expander: QueryExpander | None = None,
    ):
        self.store = store or ChromaStore()
        self.expander = expander or QueryExpander()
        self.strategy_a = StrategyA(self.store)
        self.strategy_b = StrategyB(self.store, self.expander)
        self._ingested = False

    def ingest(self, documents: list[dict] | None = None) -> int:
        """ Ingest documents into the vector store.
        """
        docs = documents or CORPUS
        self.store.add_documents(docs)
        self._ingested = True
        return len(docs)

    def search(self, query: str, strategy: str = "a", top_k: int = 3):
        """
        Search the corpus using the specified strategy."""
        if not self._ingested:
            raise RuntimeError("Pipeline has no data. Call ingest() first.")

        if strategy.lower() == "a":
            return self.strategy_a.retrieve(query, top_k=top_k)
        elif strategy.lower() == "b":
            return self.strategy_b.retrieve(query, top_k=top_k)
        else:
            raise ValueError(f"Unknown strategy '{strategy}'. Use 'a' or 'b'.")
