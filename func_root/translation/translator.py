import requests
from PioneersVision.func_root.config import (
    AZURE_TRANSLATOR_KEY,
    AZURE_TRANSLATOR_REGION
)

ENDPOINT = "https://api.cognitive.microsofttranslator.com/translate"

def translate(text, target_language):
    params = {
        "api-version": "3.0",
        "to": target_language
    }

    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_TRANSLATOR_KEY,
        "Ocp-Apim-Subscription-Region": AZURE_TRANSLATOR_REGION,
        "Content-Type": "application/json"
    }

    body = [{"text": text}]

    response = requests.post(
        ENDPOINT,
        params=params,
        headers=headers,
        json=body
    )

    response.raise_for_status()

    return response.json()[0]["translations"][0]["text"]
