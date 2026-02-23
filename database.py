import json
import os

DB_FILE = "events_db.json"

def load_events():
    """Load events from disk if the file exists"""
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_events(events):
    """Write events to disk"""
    with open(DB_FILE, "w") as f:
        json.dump(events, f, indent=4)

"""Global in-memory copy (used by the rest of your progress)"""
events = load_events()
