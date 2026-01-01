from PioneersVision.func_root.config import USE_AZURE_SPEECH
from PioneersVision.func_root.utils.validators import validate_text
from PioneersVision.func_root.speech.voices import VOICE_MAP
from PioneersVision.func_root.speech.preferences import load_preferences, save_preferences
from PioneersVision.func_root.speech.engine_azure import speak_azure
from PioneersVision.func_root.speech.engine_offline import speak_offline

def speak(text, language=None, gender=None):
    validate_text(text)

    prefs = load_preferences()

    # Use selected voice or last saved voice
    language = language or prefs.get("language", "en-US")
    gender = gender or prefs.get("gender", "female")

    voice = VOICE_MAP.get((language, gender))

    if USE_AZURE_SPEECH and voice:
        speak_azure(text, language, voice)
        save_preferences({
    "language": language,
    "gender": gender,
    "voice": voice
})

    else:
        speak_offline(text)
