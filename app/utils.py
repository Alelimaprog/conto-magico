import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
WHATSAPP_TO = os.getenv("WHATSAPP_NUMBER")

ELEVEN_API_KEY = os.getenv("ELEVENLABS_API_KEY")

def texto_para_audio(texto):
    url = "https://api.elevenlabs.io/v1/text-to-speech/OycwMuF6bqG3c4WhgKOJ/stream"
    headers = {
        "xi-api-key": ELEVEN_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": texto,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    path = "/tmp/historia.mp3"
    with open(path, "wb") as f:
        f.write(response.content)
    return path

def enviar_mensagem_whatsapp(arquivo, tipo="audio"):
    try:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(
            from_=TWILIO_FROM,
            to=WHATSAPP_TO,
            media_url="https://flushimport.com.br/audio/historia.mp3" if tipo == "audio" else None,
            body=None if tipo == "audio" else arquivo
        )
        print("Mensagem enviada:", message.sid)
        return True
    except Exception as e:
        print("[ERRO] Falha ao enviar mensagem:", e)
        return False
