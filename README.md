# Semantic RAG & Vector Search Pipeline

For assignment details see - [GenAI_RAG_VectorSearch_Assessment.pdf](https://github.com/Eviltr0N/Senior_Gen_AI_Assessment-/blob/main/GenAI_RAG_VectorSearch_Assessment.pdf)

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Generate benchmark report
python -m benchmarks.run_benchmark
```

## Architecture

```
User Query
    │
    ├─── Strategy A -> ChromaDB (direct embedding search)
    │
    └─── Strategy B -> QueryExpander (mock Gemini) --> ChromaDB (expanded query search)
```

### Key modules

 `src/embedding.py` - Embedding services (Vertex AI mock + local sentence-transformers)   
 `src/storage.py`- ChromaDB vector store wrapper    
 `src/retrieval.py`- Strategy A (raw search), Strategy B (AI-enhanced), QueryExpander   
 `src/pipeline.py`- Orchestration class managing ingest and search   
 `src/corpus.py` - data of  8 technical paragraphs on distributed systems   
  
## Deliverables

- **Source Code**: `src/` - Modular Python covering Embedding, Storage, and Retrieval
- **Tests**: `tests/` - Pytest suites verifying pipeline and GCP SDK mocking
- **Benchmark**: [retrieval_benchmark.md](https://github.com/Eviltr0N/Senior_Gen_AI_Assessment-/blob/main/retrieval_benchmark.md) — Strategy A vs B comparison for 4 queries
- **Documentation**: [documentation.md](https://github.com/Eviltr0N/Senior_Gen_AI_Assessment-/blob/main/documentation.md) - Cosine vs Euclidean rationale + Vertex AI migration guide

## Tech Stack

- **Embeddings**: sentence-transformers (`all-MiniLM-L6-v2`)
- **Vector DB**: ChromaDB (in-memory, cosine similarity)
- **Mocking**: unittest.mock (Vertex AI SDK)
- **Testing**: pytest + pytest-mock

### Note on AI Assisted Development
I used Claude opus (via Anti[gravity](https://antigravity.google/)) as a development accelerator during this assessment, primarily for boilerplate scaffolding and reviewing code structure.
