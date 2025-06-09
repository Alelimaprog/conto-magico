import os
import requests

def texto_para_audio(texto):
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    voice_id = "EXAVITQu4vr4xnSDxMaL"  # Voz padrão brasileira
    model_id = "eleven_multilingual_v2"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{{voice_id}}/stream"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": texto,
        "model_id": model_id,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    audio_path = "static/audio.mp3"
    with open(audio_path, "wb") as f:
        f.write(response.content)

    return audio_path
