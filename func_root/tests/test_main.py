from main import process_translation

test_json = {
    "status": "success",
    "translated_text": "Hello, this is a full pipeline test"
}

if __name__ == "__main__":
    result = process_translation(test_json)
    print(result)
