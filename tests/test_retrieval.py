"""
Tests for the retrieval strategies and query expander

"""

from src.retrieval import QueryExpander, StrategyA, StrategyB
from src.corpus import CORPUS
from tests.conftest import QUERY_EXPANSIONS


class TestStrategyA:
    """Tests for raw vector search Strategy A"""

    def test_retrieve_returns_results(self, populated_store):
        strategy = StrategyA(populated_store)
        results = strategy.retrieve("load balancing")
        assert len(results) == 3
        assert all("id" in r and "text" in r and "distance" in r for r in results)

    def test_retrieve_custom_top_k(self, populated_store):
        strategy = StrategyA(populated_store)
        results = strategy.retrieve("caching", top_k=2)
        assert len(results) == 2

    def test_retrieve_relevance(self, populated_store):
        """Top result for security query should be the security document."""
        strategy = StrategyA(populated_store)
        results = strategy.retrieve("OAuth JWT authentication security")
        assert results[0]["id"] == "doc_006"

    def test_results_have_metadata(self, populated_store):
        strategy = StrategyA(populated_store)
        results = strategy.retrieve("monitoring and alerting")
        assert all("metadata" in r for r in results)


class TestQueryExpander:
    """Tests for the mock-backed query expander."""

    def test_expand_known_query(self, mock_generative_model):
        expander = QueryExpander()
        query = "How does the system handle peak load?"
        expanded = expander.expand(query)
        assert expanded == QUERY_EXPANSIONS[query]

    def test_expand_calls_generate_content(self, mock_generative_model):
        expander = QueryExpander()
        expander.expand("How does the system handle peak load?")
        mock_generative_model.return_value.generate_content.assert_called_once()

    def test_expand_prompt_contains_original_query(self, mock_generative_model):
        expander = QueryExpander()
        query = "What security measures protect user data?"
        expander.expand(query)
        call_args = mock_generative_model.return_value.generate_content.call_args
        prompt = call_args[0][0]
        assert query in prompt


class TestStrategyB:
    """Tests for Strategy B"""

    def test_retrieve_returns_expanded_query(self, populated_store, mock_generative_model):
        expander = QueryExpander()
        strategy = StrategyB(populated_store, expander)
        result = strategy.retrieve("How does the system handle peak load?")

        assert "expanded_query" in result
        assert "original_query" in result
        assert "results" in result
        assert result["original_query"] == "How does the system handle peak load?"

    def test_retrieve_returns_correct_count(self, populated_store, mock_generative_model):
        expander = QueryExpander()
        strategy = StrategyB(populated_store, expander)
        result = strategy.retrieve("How does the system handle peak load?", top_k=3)
        assert len(result["results"]) == 3

    def test_expanded_query_differs_from_original(self, populated_store, mock_generative_model):
        expander = QueryExpander()
        strategy = StrategyB(populated_store, expander)
        result = strategy.retrieve("How does the system handle peak load?")
        assert result["expanded_query"] != result["original_query"]
