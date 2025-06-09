import requests
import os

API_KEY = os.getenv("ELEVENLABS_API_KEY")
voice_id = "OB6x7EbXYlhG4DDTB1XU"  # Altere aqui se quiser outra voz

def texto_para_audio(texto):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

    headers = {
        "Accept": "audio/mpeg",
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "text": texto,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()

    with open("static/audio.mp3", "wb") as f:
        f.write(response.content)

    return "static/audio.mp3"
