from PioneersVision.func_root.speech.ssml import build_ssml

ssml = build_ssml(
    text="Hello, this is a test",
    language="en-US",
    voice="en-US-JennyNeural"
)

print(ssml)
