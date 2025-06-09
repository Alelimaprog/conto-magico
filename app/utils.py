
import requests

def texto_para_audio(texto):
    url = "https://api.elevenlabs.io/v1/text-to-speech/OB6x7EbXYlhG4DDTB1XU/stream"
    headers = {
        "accept": "audio/mpeg",
        "xi-api-key": "sk_eee82b6166601c7cf13d53450b6071f0e424956a78715137",
        "Content-Type": "application/json"
    }
    payload = {
        "text": texto,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    audio_path = "/tmp/audio.mp3"
    with open(audio_path, "wb") as f:
        f.write(response.content)
    return audio_path
