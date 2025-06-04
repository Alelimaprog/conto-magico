# config/twilio.py

import os
from twilio.rest import Client

def enviar_whatsapp(numero: str, texto: str, arquivo: str = None):
    try:
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_whatsapp = os.getenv("TWILIO_WHATSAPP_FROM")
        to_whatsapp = f"whatsapp:{numero}"

        print("[DEBUG] Enviando WhatsApp...")
        print(f"De: {from_whatsapp} → Para: {to_whatsapp}")
        print(f"Texto: {texto[:80]}...")

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=texto,
            from_=from_whatsapp,
            to=to_whatsapp
        )

        print(f"[OK] Mensagem enviada. SID: {message.sid}")
        return True

    except Exception as e:
        print(f"[ERRO] Falha ao enviar WhatsApp: {e}")
        return False
