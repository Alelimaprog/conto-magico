import os
import requests
import traceback

from config.twilio import enviar_whatsapp
from config.planilha import adicionar_historico
from config.email import enviar_email

def enviar_conto_diario():
    try:
        # 1. Gerar história com OpenRouter (GPT)
        url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1/chat/completions")
        headers = {
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": "Crie uma história infantil curta (até 3 minutos), com moral educativa e personagens animais."}
            ]
        }

        resposta = requests.post(url, headers=headers, json=data)
        resposta.raise_for_status()
        historia = resposta.json()["choices"][0]["message"]["content"].strip()
        print("[OK] História gerada.")

        # 2. Enviar história como texto pelo WhatsApp
        numero = os.getenv("WHATSAPP_NUMBER")
        enviado = enviar_whatsapp(numero, historia)
        print("[OK] WhatsApp enviado.")

        # 3. Registrar na planilha (simulada)
        adicionar_historico(historia)
        print("[OK] Histórico salvo.")

        # 4. Enviar e-mail de notificação (simulado)
        enviar_email("História do dia enviada com sucesso!", historia)
        print("[OK] E-mail enviado.")

        return {"status": "success"}

    except Exception as e:
        print("[ERRO] Falha ao enviar conto:", e)
        traceback.print_exc()
        return {"status": "error"}
