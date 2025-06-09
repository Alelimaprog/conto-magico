import requests
import os

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Michelle - Young Brazilian Female

def gerar_audio(texto, nome_arquivo):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY,
    }
    payload = {
        "text": texto,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.7,
            "similarity_boost": 0.8
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    with open(nome_arquivo, "wb") as f:
        f.write(response.content)


def texto_para_audio(texto):
    nome_arquivo = "static/audio.mp3"
    gerar_audio(texto, nome_arquivo)
    return nome_arquivo
