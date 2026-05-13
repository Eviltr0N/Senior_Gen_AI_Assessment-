# Retrieval Benchmark Report

**Generated:** 2026-05-13 14:35:36

**Embedding Model:** `all-MiniLM-L6-v2` (sentence-transformers) 

**Vector Store:** ChromaDB (in-memory, cosine similarity)


---

## Query 1: "How does the system handle peak load?"

### Strategy A - Raw Vector Search

| Rank | Document ID | Distance | Snippet |
|------|-------------|----------|---------|
| 1 | `doc_001` | 0.4535 | Load balancing is a critical component in distributed systems that distributes i... |
| 2 | `doc_003` | 0.6774 | Caching strategies significantly reduce latency and database load in distributed... |
| 3 | `doc_008` | 0.7461 | Disaster recovery and fault tolerance strategies ensure business continuity when... |

### Strategy B - AI-Enhanced Retrieval

**Expanded Query:** "load balancing auto-scaling horizontal scaling traffic distribution peak load handling throughput optimization request routing health checks server provisioning dynamic scaling resource utilization"

| Rank | Document ID | Distance | Snippet |
|------|-------------|----------|---------|
| 1 | `doc_001` | 0.2144 | Load balancing is a critical component in distributed systems that distributes i... |
| 2 | `doc_003` | 0.6075 | Caching strategies significantly reduce latency and database load in distributed... |
| 3 | `doc_002` | 0.6769 | Database replication ensures data durability and high availability by maintainin... |

### Analysis

- **Strategy A top result:** `doc_001`
- **Strategy B top result:** `doc_001`
- **Result overlap:** 2/3 documents in common
- **Ranking changed:** Yes - query expansion affected retrieval order
- **New documents surfaced by Strategy B:** `doc_002`

---

## Query 2: "What security measures protect user data?"

### Strategy A - Raw Vector Search

| Rank | Document ID | Distance | Snippet |
|------|-------------|----------|---------|
| 1 | `doc_006` | 0.4594 | Authentication and authorization form the security backbone of modern applicatio... |
| 2 | `doc_008` | 0.8017 | Disaster recovery and fault tolerance strategies ensure business continuity when... |
| 3 | `doc_005` | 0.8229 | Observability in distributed systems encompasses monitoring, logging, and distri... |

### Strategy B - AI-Enhanced Retrieval

**Expanded Query:** "authentication authorization OAuth 2.0 JWT JSON Web Token encryption TLS transport layer security RBAC role-based access control ABAC single sign-on SSO field-level encryption data protection"

| Rank | Document ID | Distance | Snippet |
|------|-------------|----------|---------|
| 1 | `doc_006` | 0.2043 | Authentication and authorization form the security backbone of modern applicatio... |
| 2 | `doc_005` | 0.8605 | Observability in distributed systems encompasses monitoring, logging, and distri... |
| 3 | `doc_003` | 0.8782 | Caching strategies significantly reduce latency and database load in distributed... |

### Analysis

- **Strategy A top result:** `doc_006`
- **Strategy B top result:** `doc_006`
- **Result overlap:** 2/3 documents in common
- **Ranking changed:** Yes - query expansion affected retrieval order
- **New documents surfaced by Strategy B:** `doc_003`

---

## Query 3: "How do we ensure zero downtime during updates?"

### Strategy A - Raw Vector Search

| Rank | Document ID | Distance | Snippet |
|------|-------------|----------|---------|
| 1 | `doc_003` | 0.6944 | Caching strategies significantly reduce latency and database load in distributed... |
| 2 | `doc_007` | 0.6946 | CI/CD pipelines automate the software delivery process from code commit to produ... |
| 3 | `doc_002` | 0.7263 | Database replication ensures data durability and high availability by maintainin... |

### Strategy B - AI-Enhanced Retrieval

**Expanded Query:** "CI/CD continuous integration continuous deployment blue-green deployment canary release rolling updates zero downtime feature flags deployment strategies automated testing production deployment"

| Rank | Document ID | Distance | Snippet |
|------|-------------|----------|---------|
| 1 | `doc_007` | 0.1341 | CI/CD pipelines automate the software delivery process from code commit to produ... |
| 2 | `doc_008` | 0.6756 | Disaster recovery and fault tolerance strategies ensure business continuity when... |
| 3 | `doc_003` | 0.7327 | Caching strategies significantly reduce latency and database load in distributed... |

### Analysis

- **Strategy A top result:** `doc_003`
- **Strategy B top result:** `doc_007`
- **Result overlap:** 2/3 documents in common
- **Ranking changed:** Yes - query expansion affected retrieval order
- **New documents surfaced by Strategy B:** `doc_008`

---

## Query 4: "What happens when a database node fails?"

### Strategy A - Raw Vector Search

| Rank | Document ID | Distance | Snippet |
|------|-------------|----------|---------|
| 1 | `doc_002` | 0.5012 | Database replication ensures data durability and high availability by maintainin... |
| 2 | `doc_008` | 0.6355 | Disaster recovery and fault tolerance strategies ensure business continuity when... |
| 3 | `doc_004` | 0.6818 | Message queues enable asynchronous processing and decoupling of services in micr... |

### Strategy B - AI-Enhanced Retrieval

**Expanded Query:** "database replication failover primary replica synchronous asynchronous replication consistency conflict resolution automated failover disaster recovery RPO RTO multi-region backup data durability"

| Rank | Document ID | Distance | Snippet |
|------|-------------|----------|---------|
| 1 | `doc_002` | 0.3081 | Database replication ensures data durability and high availability by maintainin... |
| 2 | `doc_008` | 0.3668 | Disaster recovery and fault tolerance strategies ensure business continuity when... |
| 3 | `doc_003` | 0.667 | Caching strategies significantly reduce latency and database load in distributed... |

### Analysis

- **Strategy A top result:** `doc_002`
- **Strategy B top result:** `doc_002`
- **Result overlap:** 2/3 documents in common
- **Ranking changed:** Yes - query expansion affected retrieval order
- **New documents surfaced by Strategy B:** `doc_003`

---

## Summary

Strategy B (AI-Enhanced Retrieval) rewrites user queries with domain-specific technical terminology before performing the vector search, imprving retrival accuracy
The trade-off is an additional LLM call for query expansion, which adds latency. 