# config/twilio.py
from twilio.rest import Client
import os

def enviar_whatsapp(numero: str, texto: str, arquivo: str):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="whatsapp:+14155238886",  # Sandbox number
        body=texto,
        to=f"whatsapp:{numero}"
    )

    print(f"[TWILIO] Mensagem enviada para {numero}: SID = {message.sid}")
    return True
