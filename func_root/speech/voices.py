VOICE_MAP = {
    ("en-US", "female"): "en-US-JennyNeural",
    ("en-US", "male"): "en-US-GuyNeural",
    ("en-IN", "female"): "en-IN-NeerjaNeural",
    ("en-IN", "male"): "en-IN-PrabhatNeural",
    ("fr-FR", "female"): "fr-FR-DeniseNeural",
    ("de-DE", "female"): "de-DE-KatjaNeural",
    ("es-ES", "female"): "es-ES-ElviraNeural",
    ("ta-IN", "female"): "ta-IN-PallaviNeural",
    ("hi-IN", "female"): "hi-IN-SwaraNeural",
}

def get_voice(language, gender):
    return VOICE_MAP.get((language, gender))
