"""
Vector store using ChromaDB.
"""

import chromadb
from chromadb.utils import embedding_functions

from src.config import COLLECTION_NAME, LOCAL_EMBEDDING_MODEL, SIMILARITY_METRIC


class ChromaStore:
    """
    ChromaDB vector store wrapper.

    """

    def __init__(
        self,
        collection_name: str = COLLECTION_NAME,
        embedding_model: str = LOCAL_EMBEDDING_MODEL,
    ):
        self.client = chromadb.Client()  # In-memory ephemeral client
        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=embedding_model
        )
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_fn,
            metadata={"hnsw:space": SIMILARITY_METRIC},
        )

    def add_documents(self, documents: list[dict]) -> None:
        """
        Ingest documents into the vector store"""
        self.collection.add(
            ids=[doc["id"] for doc in documents],
            documents=[doc["text"] for doc in documents],
            metadatas=[doc.get("metadata", {}) for doc in documents],
        )

    def query(self, query_text: str, n_results: int = 3) -> dict:
        """
        Perform semantic search against the stored documents.

        """
        return self.collection.query(
            query_texts=[query_text],
            n_results=n_results,
            include=["documents", "distances", "metadatas"],
        )

    @property
    def count(self) -> int:
        """Return the number of docs in collection."""
        return self.collection.count()
