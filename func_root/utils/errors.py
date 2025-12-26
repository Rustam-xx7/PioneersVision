
class SpeechEngineError(Exception):
    """
    Raised when Azure Speech or Offline TTS fails
    """
    pass


class TranslationError(Exception):
    """
    Raised when translation service fails
    """
    pass


class ValidationError(Exception):
    """
    Raised when input validation fails
    """
    pass
class InvalidInputError(Exception):
    """Raised when input JSON is invalid"""
    pass