from PioneersVision.func_root.speech.speaker import speak
from func_root.translation.translator import translate

asl_text = "Welcome to the sign language translation app"

print("Detected text:", asl_text)

translated = translate(asl_text, "fr")
print("Translated text:", translated)

speak(translated, "fr-FR", "female")
