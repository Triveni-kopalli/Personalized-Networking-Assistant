import pytest
from unittest.mock import patch, MagicMock

@patch("backend.services.event_analyzer.pipeline")
def test_event_analyzer(mock_pipeline):
    # Mock the pipeline behavior
    mock_classifier = MagicMock()
    mock_classifier.return_value = {
        "labels": ["AI & Machine Learning", "Technology & Software", "Finance"],
        "scores": [0.9, 0.8, 0.7]
    }
    mock_pipeline.return_value = mock_classifier
    
    # Import inside after patching to apply the mock
    from backend.services.event_analyzer import EventAnalyzer
    
    analyzer = EventAnalyzer()
    themes = analyzer.analyze("A big AI conference for the future of tech.", top_k=2)
    
    assert len(themes) == 2
    assert themes == ["AI & Machine Learning", "Technology & Software"]

    # Test empty input
    themes_empty = analyzer.analyze("")
    assert themes_empty == []
