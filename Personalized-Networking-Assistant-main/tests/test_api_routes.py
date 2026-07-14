import pytest
from fastapi.testclient import TestClient
from backend.main import app

# Since we use mocking in unit tests, we'd ideally mock the HF pipelines here too to make them fast.
# We'll just patch the services at the API level.

client = TestClient(app)

@pytest.fixture(autouse=True)
def mock_services(monkeypatch):
    # Mock event analyzer
    class MockEventAnalyzer:
        def analyze(self, text):
            return ["AI", "Tech"]
    monkeypatch.setattr("backend.routes.api.event_analyzer", MockEventAnalyzer())
    
    # Mock topic generator
    class MockTopicGenerator:
        def generate_starters(self, themes, interests, num_starters=3):
            return ["Starter 1.", "Starter 2.", "Starter 3."]
    monkeypatch.setattr("backend.routes.api.topic_generator", MockTopicGenerator())
    
    # Mock fact checker
    from backend.services.fact_checker import FactCheckResult
    def mock_get_fact_check(query):
        return FactCheckResult(summary=f"Summary for {query}", source_url="http://example.com")
    monkeypatch.setattr("backend.routes.api.get_fact_check", mock_get_fact_check)
    
    # Mock loggers
    monkeypatch.setattr("backend.routes.api.log_generation", lambda **kw: "test-id-123")
    monkeypatch.setattr("backend.routes.api.log_feedback", lambda *a: True)
    monkeypatch.setattr("backend.routes.api.get_history", lambda: [])

def test_analyze_event():
    response = client.post("/api/v1/analyze-event", json={"event_description": "Tech conference"})
    assert response.status_code == 200
    assert response.json() == {"themes": ["AI", "Tech"]}

def test_generate_conversation():
    response = client.post("/api/v1/generate-conversation", json={
        "event_description": "Tech conference",
        "interests": ["startups"]
    })
    assert response.status_code == 200
    data = response.json()
    assert data["generation_id"] == "test-id-123"
    assert data["themes"] == ["AI", "Tech"]
    assert len(data["starters"]) == 3

def test_fact_check():
    response = client.get("/api/v1/fact-check", params={"query": "AI"})
    assert response.status_code == 200
    assert response.json()["summary"] == "Summary for AI"

def test_feedback():
    response = client.post("/api/v1/feedback", json={"starter_id": "test-id-123", "useful": True})
    assert response.status_code == 200
    assert response.json()["success"] is True

def test_history():
    response = client.get("/api/v1/history")
    assert response.status_code == 200
    assert response.json() == {"history": []}
