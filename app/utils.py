import os
import requests
from datetime import datetime

ELEVEN_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVEN_VOICE_ID = "OB6x7EbXYlhG4DDTB1XU"

def texto_para_audio(texto):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_VOICE_ID}/stream"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVEN_API_KEY
    }

    payload = {
        "text": texto,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    filename = f"audio_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"
    filepath = os.path.join("/tmp", filename)
    with open(filepath, "wb") as f:
        f.write(response.content)

    return filepath
