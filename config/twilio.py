# config/twilio.py

import os
from twilio.rest import Client

def enviar_whatsapp(numero: str, texto: str, arquivo: str = None):
    try:
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_whatsapp_number = "whatsapp:+14155238886"  # padrão do sandbox
        to_whatsapp_number = f"whatsapp:{numero}"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=texto,
            from_=from_whatsapp_number,
            to=to_whatsapp_number
        )

        print(f"[OK] WhatsApp enviado. SID: {message.sid}")
        return True

    except Exception as e:
        print("[ERRO] Falha ao enviar WhatsApp:", e)
        return False
