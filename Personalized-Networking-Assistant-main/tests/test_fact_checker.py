import pytest
from unittest.mock import patch, MagicMock
from backend.services.fact_checker import get_fact_check

@patch("backend.services.fact_checker.wikipedia")
def test_get_fact_check_success(mock_wikipedia):
    # Mock wikipedia.search
    mock_wikipedia.search.return_value = ["Generative AI"]
    
    # Mock wikipedia.page
    mock_page = MagicMock()
    mock_page.url = "https://en.wikipedia.org/wiki/Generative_AI"
    mock_wikipedia.page.return_value = mock_page
    
    # Mock wikipedia.summary
    mock_wikipedia.summary.return_value = "Generative AI is a type of AI system."
    
    result = get_fact_check("Generative AI")
    
    assert result.error is None
    assert result.summary == "Generative AI is a type of AI system."
    assert result.source_url == "https://en.wikipedia.org/wiki/Generative_AI"

@patch("backend.services.fact_checker.wikipedia")
def test_get_fact_check_not_found(mock_wikipedia):
    mock_wikipedia.search.return_value = []
    
    result = get_fact_check("Some weird unknown topic 123456")
    
    assert result.error == "Page not found"
    assert "No relevant information found" in result.summary
