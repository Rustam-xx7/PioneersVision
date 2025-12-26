import os
from dotenv import load_dotenv

load_dotenv()

def health_check():
    required_vars = [
        "SPEECH_KEY",
        "SPEECH_REGION",
        "TRANSLATOR_KEY",
        "TRANSLATOR_ENDPOINT",
        "TRANSLATOR_REGION"
    ]

    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        return {
            "status": "unhealthy",
            "missing_env_vars": missing
        }

    return {
        "status": "healthy",
        "message": "All Azure services configured"
    }

