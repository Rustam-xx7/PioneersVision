def validate_text(text):
    if not isinstance(text, str):
        raise ValueError("Text must be string")
    if not text.strip():
        raise ValueError("Text cannot be empty")
