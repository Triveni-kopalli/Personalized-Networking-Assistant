import json
import os
import uuid
from datetime import datetime

HISTORY_FILE = "data/history.json"

def init_history_file():
    """Ensure the history file exists and contains an empty list if it's new."""
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'w') as f:
            json.dump([], f)

def log_generation(event_description: str, interests: list[str], themes: list[str], starters: list[str]) -> str:
    """Log a generated conversation starter event. Returns the unique generation ID."""
    init_history_file()
    
    generation_id = str(uuid.uuid4())
    entry = {
        "id": generation_id,
        "timestamp": datetime.utcnow().isoformat(),
        "event_description": event_description,
        "interests": interests,
        "themes": themes,
        "starters": starters,
        "useful": None  # Will be updated by feedback
    }
    
    try:
        with open(HISTORY_FILE, 'r') as f:
            history = json.load(f)
    except json.JSONDecodeError:
        history = []
        
    history.append(entry)
    
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)
        
    return generation_id

def get_history() -> list[dict]:
    """Retrieve all past generation history."""
    init_history_file()
    try:
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
