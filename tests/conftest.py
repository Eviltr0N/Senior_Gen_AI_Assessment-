"""
Shared pytest fixtures and mock setup for the RAG pipeline tests
"""

import pytest
from unittest.mock import MagicMock, patch

from sentence_transformers import SentenceTransformer

from src.config import LOCAL_EMBEDDING_MODEL
from src.storage import ChromaStore
from src.corpus import CORPUS



#  query expansions for strategy B benchmarking

QUERY_EXPANSIONS = {
    "How does the system handle peak load?": (
        "load balancing auto-scaling horizontal scaling traffic distribution "
        "peak load handling throughput optimization request routing health checks "
        "server provisioning dynamic scaling resource utilization"
    ),
    "What security measures protect user data?": (
        "authentication authorization OAuth 2.0 JWT JSON Web Token encryption "
        "TLS transport layer security RBAC role-based access control ABAC "
        "single sign-on SSO field-level encryption data protection"
    ),
    "How do we ensure zero downtime during updates?": (
        "CI/CD continuous integration continuous deployment blue-green deployment "
        "canary release rolling updates zero downtime feature flags deployment "
        "strategies automated testing production deployment"
    ),
    "What happens when a database node fails?": (
        "database replication failover primary replica synchronous asynchronous "
        "replication consistency conflict resolution automated failover disaster "
        "recovery RPO RTO multi-region backup data durability"
    ),
}


# Fixtures

@pytest.fixture
def local_model():
    """Load the sentence-transformers model"""
    return SentenceTransformer(LOCAL_EMBEDDING_MODEL)


@pytest.fixture
def chroma_store():
    """Create a ChromaDB store for each test."""
    import uuid
    unique_name = f"test_{uuid.uuid4().hex[:8]}"
    return ChromaStore(collection_name=unique_name)


@pytest.fixture
def populated_store(chroma_store):
    """ChromaDB store pre-loaded with the full data."""
    chroma_store.add_documents(CORPUS)
    return chroma_store


@pytest.fixture
def mock_vertex_embedding(local_model):
    """
    Mock vertexai.language_models.TextEmbeddingModel.

    capture from_pretrained() and get_embeddings() calls and route them to the  sentence-transformers model.
    """
    def fake_get_embeddings(texts):
        vectors = local_model.encode(texts)
        results = []
        for vec in vectors:
            mock_emb = MagicMock()
            mock_emb.values = vec.tolist()
            results.append(mock_emb)
        return results

    with patch("src.embedding.TextEmbeddingModel") as MockModel:
        mock_instance = MagicMock()
        mock_instance.get_embeddings.side_effect = fake_get_embeddings
        MockModel.from_pretrained.return_value = mock_instance
        yield MockModel


@pytest.fixture
def mock_generative_model():
    """
    returns deterministic expanded queries from the QUERY_EXPANSIONS dict.

    """
    def fake_generate_content(prompt):
        # Extract the original query from the prompt
        for original, expanded in QUERY_EXPANSIONS.items():
            if original in prompt:
                mock_response = MagicMock()
                mock_response.text = expanded
                return mock_response
                
        # falback: return the prompt itself (shouldn't happen in tests)
        mock_response = MagicMock()
        mock_response.text = prompt.split("Original query: ")[-1] if "Original query: " in prompt else prompt
        return mock_response

    with patch("src.retrieval.GenerativeModel") as MockGenModel:
        mock_instance = MagicMock()
        mock_instance.generate_content.side_effect = fake_generate_content
        MockGenModel.return_value = mock_instance
        yield MockGenModel
