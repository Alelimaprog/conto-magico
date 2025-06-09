import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Chaves de API
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
TWILIO_WHATSAPP_TO = os.getenv("TWILIO_WHATSAPP_TO")

# Voz padrão temporária para português
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel (ElevenLabs)


def gerar_audio(texto: str, output_path: str):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": texto,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.3,
            "similarity_boost": 0.8
        }
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    with open(output_path, "wb") as f:
        f.write(response.content)


def enviar_mensagem_whatsapp():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    audio_url = "https://conto-magico-production.up.railway.app/static/audio.mp3"

    message = client.messages.create(
        from_=f"whatsapp:{TWILIO_WHATSAPP_FROM}",
        to=f"whatsapp:{TWILIO_WHATSAPP_TO}",
        media_url=[audio_url]
    )
    return message.sid


def texto_para_audio(historia):
    audio_path = "static/audio.mp3"
    gerar_audio(historia, audio_path)
    return audio_path
