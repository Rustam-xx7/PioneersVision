# speech/engine_offline.py

import pyttsx3
from func_root.utils.logger import logger

_engine = pyttsx3.init()


def speak_offline(text):
    logger.info("Offline TTS started")
    _engine.say(text)
    _engine.runAndWait()
    logger.info("Offline TTS finished")
