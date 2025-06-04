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
        # 1. Gerar conto com DeepSeek API (formato compatível com OpenAI)
        client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com/v1"
        )

        prompt = "Crie uma história infantil curta (até 3 minutos), com moral educativa e personagens animais."
        resposta = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )
        historia = resposta.choices[0].message.content.strip()
        print("[OK] História gerada.")

        # 2. Converter para áudio com ElevenLabs
        audio = generate(
            api_key=os.getenv("ELEVEN_API_KEY"),
            voice="Rachel",
            text=historia
        )
        caminho_arquivo = "/tmp/audio.mp3"
        save(audio, caminho_arquivo)
        print("[OK] Áudio gerado e salvo.")

        # 3. Enviar por WhatsApp (Twilio)
        numero = os.getenv("WHATSAPP_NUMBER")
        enviado = enviar_whatsapp(numero, historia, caminho_arquivo)
        print("[OK] WhatsApp enviado.")

        # 4. Registrar em planilha
        adicionar_historico(historia)
        print("[OK] Histórico salvo.")

        # 5. Enviar e-mail de notificação
        enviar_email("História do dia enviada com sucesso!", historia)
        print("[OK] E-mail enviado.")

        return {"status": "success"}

    except Exception as e:
        print("[ERRO] Falha ao enviar conto:", e)
        traceback.print_exc()
        return {"status": "error"}
