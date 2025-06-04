import os
import requests
import traceback
from openai import OpenAI
from elevenlabs import generate, save
from config.planilha import adicionar_historico
from config.email import enviar_email
from config.twilio import enviar_whatsapp

def enviar_conto_diario():
    try:
        # 1. Gerar conto com OpenRouter (OpenAI compatível)
        headers = {
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "openrouter/openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": "Crie uma história infantil curta (até 3 minutos), com moral educativa e personagens animais."
                }
            ]
        }

        resposta = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        resposta.raise_for_status()
        historia = resposta.json()["choices"][0]["message"]["content"].strip()
        print("[OK] História gerada.")

        # 2. Converter para áudio com ElevenLabs usando Voice ID
        audio = generate(
            api_key=os.getenv("ELEVEN_API_KEY"),
            voice="OB6x7EbXYlhG4DDTB1XU",  # Voice ID da voz feminina em português
            text=historia
        )
        caminho_arquivo = "/tmp/audio.mp3"
        save(audio, caminho_arquivo)
        print("[OK] Áudio gerado e salvo.")

        # 3. Enviar por WhatsApp
        numero = os.getenv("WHATSAPP_NUMBER")
        enviado = enviar_whatsapp(numero, historia, caminho_arquivo)
        print("[OK] WhatsApp enviado.")

        # 4. Registrar em planilha
        adicionar_historico(historia)
        print("[OK] Histórico salvo.")

        # 5. Enviar e-mail
        enviar_email("História do dia enviada com sucesso!", historia)
        print("[OK] E-mail enviado.")

        return {"status": "success"}

    except Exception as e:
        print("[ERRO] Falha ao enviar conto:", e)
        traceback.print_exc()
        return {"status": "error"}
