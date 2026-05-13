"""
embedding service for the RAG.

VertexEmbeddingService: ertex AI SDK (mocked in tests).
LocalEmbeddingService:  sentence-transformers implementation.

"""

from sentence_transformers import SentenceTransformer
from vertexai.language_models import TextEmbeddingModel

from src.config import LOCAL_EMBEDDING_MODEL, VERTEX_EMBEDDING_MODEL


class VertexEmbeddingService:
    """embedding service for the Vertex AI SDK"""

    def __init__(self, model_name: str = VERTEX_EMBEDDING_MODEL):
        self.model_name = model_name
        self.model = TextEmbeddingModel.from_pretrained(model_name)

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Generate embeddings via Vertex AI API (mock)"""
        embeddings = self.model.get_embeddings(texts)
        return [e.values for e in embeddings]


class LocalEmbeddingService:
    """
    embedding service using sentence-transformers directly."""

    def __init__(self, model_name: str = LOCAL_EMBEDDING_MODEL):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: list[str]) -> list[list[float]]:
        """embeddings using the local sentence-transformers.
        """
        return self.model.encode(texts).tolist()
