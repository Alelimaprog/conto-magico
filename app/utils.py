import os
import requests

from twilio.rest import Client

def enviar_mensagem_whatsapp(mensagem, numero_destino, audio_path=None):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER")

    client = Client(account_sid, auth_token)

    if audio_path:
        message = client.messages.create(
            body=mensagem,
            from_=f"whatsapp:{twilio_whatsapp_number}",
            to=f"whatsapp:{numero_destino}",
        )
        media = client.messages.create(
            media_url=[audio_path],
            from_=f"whatsapp:{twilio_whatsapp_number}",
            to=f"whatsapp:{numero_destino}",
        )
        return media.sid
    else:
        message = client.messages.create(
            body=mensagem,
            from_=f"whatsapp:{twilio_whatsapp_number}",
            to=f"whatsapp:{numero_destino}",
        )
        return message.sid

def texto_para_audio(texto):
    url = "https://api.elevenlabs.io/v1/text-to-speech/OB6x7EbXYlhG4DDTB1XU/stream"

    headers = {
        "xi-api-key": "sk_eee82b6166601c7cf13d53450b6071f0e424956a78715137",
        "Content-Type": "application/json"
    }

    body = {
        "text": texto,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, json=body, stream=True)
    response.raise_for_status()

    output_path = "app/static/audio/audio.mp3"
    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=4096):
            f.write(chunk)

    return "/" + output_path
