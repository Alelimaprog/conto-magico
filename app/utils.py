
import requests
import os

def enviar_mensagem_whatsapp(mensagem, numero_destino):
    from twilio.rest import Client
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    mensagem = client.messages.create(
        from_='whatsapp:' + os.getenv("TWILIO_PHONE_NUMBER"),
        body=mensagem,
        to='whatsapp:' + numero_destino
    )
    return mensagem.sid

def texto_para_audio(texto):
    api_key = os.getenv("ELEVEN_API_KEY")
    voice_id = "OB6x7EbXYlhG4DDTB1XU"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": texto,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    audio_path = "/tmp/audio.mp3"
    with open(audio_path, "wb") as f:
        f.write(response.content)

    return audio_path
