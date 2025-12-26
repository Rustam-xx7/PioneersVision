import json
from pathlib import Path

PREF_FILE = Path("ui/user_preferences.json")

def load_preferences():
    if PREF_FILE.exists():
        return json.loads(PREF_FILE.read_text(encoding="utf-8"))
    return {}

def save_preferences(data):
    PREF_FILE.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8"
    )
