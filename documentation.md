# Documentation

## Question 1: Similarity Metric - Cosine vs Euclidean

### Our Choice: Cosine Similarity

This pipeline uses **cosine similarity** as the distance metric for vector search in ChromaDB (configured via `hnsw:space: "cosine"`).

### What Each Metric Measures

| Metric | What It Measures |
|--------|------------------|
| **Cosine Similarity** | Angle between two vectors (direction) |
| **Euclidean Distance** | Absolute straight-line distance between points |

### Why Cosine Similarity Is Better for This Use Case

- **Magnitude Invariance**: Cosine similarity only cares about the *direction* of vectors, not their magnitude. A short document and a long document about the same topic will have similar angles even if their vector magnitudes differ. Euclidean distance would penalize this magnitude difference, treating them as dissimilar.

- **Industry Standard**: Cosine similarity is the de facto metric for semantic text search in production systems including Google's Vertex AI Vector Search, OpenAI's embeddings, and Pinecone.

- **Better for Sparse Overlap**: In information retrieval, documents may share meaning without sharing exact vocabulary. Cosine similarity captures this directional similarity better than Euclidean distance, which can be misleading in high-dimensional spaces (curse of dimensionality).

---

## Question 2: Migration to Vertex AI Vector Search

### Current Architecture (Local)

```
User Query -> Query expantion -> sentence-transformers (local) --> ChromaDB --> Retrived Results
```

### Target Production Architecture  on GCP

```
User Query -> Query expantion ->Vertex AI textembedding-gecko -> Vertex AI Vector Search → Retrived Results
```

### Migration Steps

1. Replace Local Embeddings with Vertex AI API

2. Replace ChromaDB with Vertex AI Vector Search

3. Replace Mock GenerativeModel with Real Gemini API


### Key Point

The local pipeline mirrors the production architecture by design. The `VertexEmbeddingService` and `QueryExpander` already use the Vertex AI SDK interfaces, migration is just a matter of removing mocks and configuring GCP credentials, not rewriting application logic. 
