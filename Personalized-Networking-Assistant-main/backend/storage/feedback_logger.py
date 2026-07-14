import json
import os
from datetime import datetime
from .history_logger import HISTORY_FILE, init_history_file

FEEDBACK_FILE = "data/feedback.json"

def init_feedback_file():
    os.makedirs(os.path.dirname(FEEDBACK_FILE), exist_ok=True)
    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, 'w') as f:
            json.dump([], f)

def log_feedback(generation_id: str, useful: bool) -> bool:
    """Log feedback and update history if possible."""
    init_feedback_file()
    
    feedback_entry = {
        "generation_id": generation_id,
        "useful": useful,
        "timestamp": datetime.utcnow().isoformat()
    }
    
    # Update feedback.json
    try:
        with open(FEEDBACK_FILE, 'r') as f:
            feedbacks = json.load(f)
    except json.JSONDecodeError:
        feedbacks = []
        
    feedbacks.append(feedback_entry)
    
    with open(FEEDBACK_FILE, 'w') as f:
        json.dump(feedbacks, f, indent=2)
        
    # Also attempt to update the history.json record
    init_history_file()
    try:
        with open(HISTORY_FILE, 'r') as f:
            history = json.load(f)
            
        updated = False
        for entry in history:
            if entry.get("id") == generation_id:
                entry["useful"] = useful
                updated = True
                break
                
        if updated:
            with open(HISTORY_FILE, 'w') as f:
                json.dump(history, f, indent=2)
                
        return updated
    except Exception:
        return False
