from func_root.speech.speaker import speak
from func_root.speech.health import health_check
from func_root.utils.errors import InvalidInputError
from func_root.utils.logger import logger


def process_translation(json_input: dict):
    """
    Common entry point for translated text → speech
    Used by:
    - Camera pipeline
    - API / Flask
    - Future UI
    """

    logger.info("process_translation called")

    if not health_check():
        raise RuntimeError("Speech service unhealthy")

    if not isinstance(json_input, dict):
        raise InvalidInputError("Input must be a dictionary")

    if "translated_text" not in json_input:
        raise InvalidInputError("Missing translated_text")

    text = json_input["translated_text"]

    if not isinstance(text, str) or not text.strip():
        raise InvalidInputError("translated_text must be a non-empty string")

    speak(text)

    return {
        "status": "speech_generated",
        "spoken_text": text
    }
