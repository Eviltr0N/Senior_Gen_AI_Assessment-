"""
Technical data corpus for the RAG pipeline. 8 paragraphs covering distributed systems and cloud infrastructure.
"""

CORPUS = [
    {
        "id": "doc_001",
        "text": (
            "Load balancing is a critical component in distributed systems that distributes "
            "incoming network traffic across multiple servers to ensure no single server bears "
            "too much demand. Modern load balancers use algorithms such as round-robin, least "
            "connections, and weighted distribution to optimize resource utilization. When "
            "traffic spikes occur, horizontal auto-scaling provisions additional server "
            "instances dynamically, and the load balancer automatically routes requests to "
            "these new nodes. Health checks continuously monitor server availability, removing "
            "unhealthy instances from the pool to maintain high availability and minimize "
            "response latency during peak load conditions."
        ),
        "metadata": {"topic": "load_balancing", "section": "infrastructure"},
    },
    {
        "id": "doc_002",
        "text": (
            "Database replication ensures data durability and high availability by maintaining "
            "synchronized copies of data across multiple nodes. In a primary-replica setup, "
            "write operations are directed to the primary node and asynchronously propagated "
            "to replicas. Synchronous replication guarantees strong consistency but introduces "
            "latency, while asynchronous replication offers better performance at the cost of "
            "eventual consistency. Conflict resolution strategies such as last-writer-wins and "
            "vector clocks handle concurrent updates in multi-primary configurations. "
            "Automated failover detects primary node failures and promotes a replica to primary "
            "within seconds, minimizing downtime."
        ),
        "metadata": {"topic": "database_replication", "section": "data"},
    },
    {
        "id": "doc_003",
        "text": (
            "Caching strategies significantly reduce latency and database load in distributed "
            "applications. Redis and Memcached serve as in-memory data stores for frequently "
            "accessed data, implementing patterns like cache-aside, write-through, and "
            "write-behind. Content Delivery Networks (CDNs) cache static assets at edge "
            "locations geographically close to users, reducing round-trip times. Cache "
            "invalidation remains one of the hardest problems in computer science — strategies "
            "include time-to-live (TTL) expiration, event-driven invalidation, and versioned "
            "cache keys. Multi-tier caching architectures combine L1 application-level caches "
            "with L2 distributed caches for optimal hit rates."
        ),
        "metadata": {"topic": "caching", "section": "performance"},
    },
    {
        "id": "doc_004",
        "text": (
            "Message queues enable asynchronous processing and decoupling of services in "
            "microservice architectures. Systems like Apache Kafka, RabbitMQ, and Amazon SQS "
            "buffer requests between producers and consumers, allowing each to scale "
            "independently. Dead letter queues capture messages that fail processing after "
            "multiple retry attempts, preventing message loss. Event-driven architectures "
            "use publish-subscribe patterns to broadcast state changes across services. "
            "Back-pressure mechanisms throttle producers when consumers cannot keep up, "
            "preventing queue overflow. Message ordering guarantees and exactly-once delivery "
            "semantics are critical for financial transaction processing."
        ),
        "metadata": {"topic": "message_queues", "section": "architecture"},
    },
    {
        "id": "doc_005",
        "text": (
            "Observability in distributed systems encompasses monitoring, logging, and "
            "distributed tracing. Prometheus collects time-series metrics while Grafana "
            "provides visualization dashboards for real-time system health monitoring. "
            "Structured logging with correlation IDs enables tracing requests across "
            "microservice boundaries. Tools like Jaeger and Zipkin implement the OpenTelemetry "
            "standard for distributed tracing, revealing latency bottlenecks in complex call "
            "chains. Alerting systems trigger notifications based on threshold breaches, "
            "anomaly detection, and SLO burn rate calculations. Effective observability "
            "reduces mean time to detection (MTTD) and mean time to resolution (MTTR) "
            "during production incidents."
        ),
        "metadata": {"topic": "observability", "section": "operations"},
    },
    {
        "id": "doc_006",
        "text": (
            "Authentication and authorization form the security backbone of modern "
            "applications. OAuth 2.0 provides delegated authorization through access tokens, "
            "while OpenID Connect adds an identity layer for single sign-on (SSO). JSON Web "
            "Tokens (JWTs) encode user claims and are cryptographically signed to prevent "
            "tampering. Role-Based Access Control (RBAC) assigns permissions based on user "
            "roles, while Attribute-Based Access Control (ABAC) evaluates policies against "
            "user attributes, resource properties, and environmental conditions. Transport "
            "Layer Security (TLS) encrypts data in transit, and field-level encryption "
            "protects sensitive data at rest in databases."
        ),
        "metadata": {"topic": "security", "section": "security"},
    },
    {
        "id": "doc_007",
        "text": (
            "CI/CD pipelines automate the software delivery process from code commit to "
            "production deployment. Continuous Integration triggers automated builds and "
            "unit tests on every commit, catching regressions early. Continuous Deployment "
            "extends this by automatically deploying passing builds to production. Blue-green "
            "deployments maintain two identical environments, switching traffic atomically "
            "between them. Canary releases gradually route a small percentage of traffic to "
            "the new version, monitoring error rates before full rollout. Rolling updates "
            "replace instances incrementally, ensuring zero downtime. Feature flags enable "
            "decoupling deployment from release, allowing incomplete features to exist safely "
            "in production behind toggles."
        ),
        "metadata": {"topic": "cicd", "section": "devops"},
    },
    {
        "id": "doc_008",
        "text": (
            "Disaster recovery and fault tolerance strategies ensure business continuity when "
            "infrastructure failures occur. Recovery Point Objective (RPO) defines maximum "
            "acceptable data loss, while Recovery Time Objective (RTO) sets the target for "
            "service restoration. Multi-region deployments replicate services across "
            "geographically separated data centers, enabling failover when an entire region "
            "goes offline. Circuit breakers prevent cascading failures by stopping requests "
            "to failing downstream services. Chaos engineering practices, popularized by "
            "Netflix's Chaos Monkey, proactively inject failures to validate system "
            "resilience. Regular backup testing and disaster recovery drills ensure recovery "
            "procedures work when needed most."
        ),
        "metadata": {"topic": "disaster_recovery", "section": "reliability"},
    },
]
