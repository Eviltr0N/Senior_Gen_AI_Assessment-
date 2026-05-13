"""
Configuration constants for the RAG pipeline.
"""

# Embedding model used by sentence-transformers locally
LOCAL_EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Vertex AI model name (used in production code, mocked locally)
VERTEX_EMBEDDING_MODEL = "textembedding-gecko"
VERTEX_GENERATIVE_MODEL = "gemini-1.5-flash"

# ChromaDB settings
COLLECTION_NAME = "rag_documents"
SIMILARITY_METRIC = "cosine"  # Options: "cosine", "l2" (euclidean), "ip" (inner product)

# Retrieval defaults
DEFAULT_TOP_K = 3
