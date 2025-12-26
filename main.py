
import json
from func_root.speech.speaker import speak
from func_root.utils.logger import logger
from func_root.utils.errors import InvalidInputError
from func_root.speech.health import health_check

def process_translation(json_input: dict):
    """
    Entry point for Flask JSON input
    """

    logger.info("Received JSON input")

    if not health_check():
        raise RuntimeError("Speech service unhealthy")

    if "translated_text" not in json_input:
        raise InvalidInputError("Missing translated_text in JSON")

    text = json_input["translated_text"]

    print("Detected text:", text)   # ✅ THIS IS WHERE IT GOES

    speak(text)

    return {
        "status": "speech_generated",
        "spoken_text": text
    }
