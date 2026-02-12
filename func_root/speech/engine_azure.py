# speech/engine_azure.py
import azure.cognitiveservices.speech as speechsdk
from func_root.config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION
from func_root.speech.ssml import build_ssml
from func_root.utils.logger import logger
from func_root.utils.errors import SpeechEngineError


def speak_azure(text, language, voice):
    try:
        speech_config = speechsdk.SpeechConfig(
            subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION
        )

        # 🔊 FORCE AUDIO OUTPUT TO SPEAKERS (THIS WAS MISSING)
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

        synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=speech_config, audio_config=audio_config
        )

        ssml = build_ssml(text, language, voice)

        result = synthesizer.speak_ssml_async(ssml).get()

        if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
            raise SpeechEngineError("Azure speech failed")

        logger.info(f"Azure speech success | {voice}")

    except Exception as e:
        logger.error(f"Azure error: {e}")
        raise SpeechEngineError(str(e))

