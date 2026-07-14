from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.services.event_analyzer import event_analyzer
from backend.services.topic_generator import topic_generator
from backend.services.fact_checker import get_fact_check, FactCheckResult
from backend.storage.history_logger import log_generation, get_history
from backend.storage.feedback_logger import log_feedback

router = APIRouter()

class AnalyzeEventRequest(BaseModel):
    event_description: str

class GenerateConversationRequest(BaseModel):
    event_description: str
    interests: list[str] = []

class FeedbackRequest(BaseModel):
    starter_id: str
    useful: bool

@router.post("/analyze-event")
def analyze_event(request: AnalyzeEventRequest):
    if not request.event_description:
        raise HTTPException(status_code=400, detail="event_description cannot be empty")
    themes = event_analyzer.analyze(request.event_description)
    return {"themes": themes}

@router.post("/generate-conversation")
def generate_conversation(request: GenerateConversationRequest):
    if not request.event_description:
        raise HTTPException(status_code=400, detail="event_description cannot be empty")
        
    themes = event_analyzer.analyze(request.event_description)
    starters = topic_generator.generate_starters(themes=themes, interests=request.interests)
    
    # Log this generation
    generation_id = log_generation(
        event_description=request.event_description,
        interests=request.interests,
        themes=themes,
        starters=starters
    )
    
    return {
        "generation_id": generation_id,
        "themes": themes,
        "starters": starters
    }

@router.get("/fact-check", response_model=FactCheckResult)
def fact_check(query: str):
    if not query:
        raise HTTPException(status_code=400, detail="query parameter is required")
    return get_fact_check(query)

@router.post("/feedback")
def feedback(request: FeedbackRequest):
    success = log_feedback(request.starter_id, request.useful)
    if not success:
        # Note: We still return 200 even if ID not found, but indicate success status
        return {"success": False, "message": "Could not update history record."}
    return {"success": True}

@router.get("/history")
def history():
    return {"history": get_history()}
