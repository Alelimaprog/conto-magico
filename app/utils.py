import os
from twilio.rest import Client

# Carrega as variáveis de ambiente
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")  # Ex: "whatsapp:+14155238886"
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")            # Ex: "whatsapp:+55..."

def enviar_mensagem_whatsapp(texto: str):
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_FROM, WHATSAPP_NUMBER]):
        print("[ERRO] Variáveis Twilio não configuradas corretamente")
        return False

    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=texto,
            from_=TWILIO_WHATSAPP_FROM,
            to=WHATSAPP_NUMBER if WHATSAPP_NUMBER.startswith("whatsapp:") else f"whatsapp:{WHATSAPP_NUMBER}"
        )
        print(f"[SUCESSO] Mensagem enviada. SID: {message.sid}")
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao enviar mensagem: {e}")
        return False
