from func_root.translation.translator import translate

if __name__ == "__main__":
    text = "Welcome to the app"
    translated = translate(text, "fr")
    print("Translated text:", translated)
