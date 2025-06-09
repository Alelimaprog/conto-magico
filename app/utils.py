import requests
import os
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "ErXwobaYiN019PkySvjV"  # Antonio - voz padrão pt-br da ElevenLabs

def texto_para_audio(texto: str) -> str:
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": texto,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    audio_path = "app/static/audio.mp3"
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)
    with open(audio_path, "wb") as f:
        f.write(response.content)
    return "/" + audio_path
