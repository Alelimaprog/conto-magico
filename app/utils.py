import os
import requests
from twilio.rest import Client

# Variáveis do OpenRouter (IA)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")

# Variáveis do Twilio (WhatsApp)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")

def gerar_conto(mensagem_usuario):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": "Você é um contador de histórias infantis criativas, educativas e com uma moral positiva no final."},
            {"role": "user", "content": mensagem_usuario}
        ]
    }

    try:
        response = requests.post(OPENROUTER_BASE_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        print("[ERRO gerar_conto]", e)
        return None

def enviar_mensagem_whatsapp(texto: str):
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_FROM, WHATSAPP_NUMBER]):
        print("[ERRO] Variáveis Twilio não configuradas corretamente")
        return False

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    try:
        message = client.messages.create(
            body=texto,
            from_=TWILIO_WHATSAPP_FROM,
            to=f"whatsapp:{WHATSAPP_NUMBER}" if not WHATSAPP_NUMBER.startswith("whatsapp:") else WHATSAPP_NUMBER
        )
        print(f"[SUCESSO] Mensagem enviada. SID: {message.sid}")
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao enviar mensagem: {e}")
        return False
