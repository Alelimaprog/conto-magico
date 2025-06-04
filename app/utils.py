import os
import requests
import traceback
from elevenlabs import generate, save
from config.planilha import adicionar_historico
from config.email import enviar_email
from config.twilio import enviar_whatsapp

def enviar_conto_diario():
    try:
        # 1. Gerar conto com DeepSeek via requests
        api_key = os.getenv("DEEPSEEK_API_KEY")
        prompt = "Crie uma história infantil curta (até 3 minutos), com moral educativa e personagens animais."

        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        response.raise_for_status()
        historia = response.json()["choices"][0]["message"]["content"].strip()
        print("[OK] História gerada.")

        # 2. Gerar áudio com ElevenLabs
        audio = generate(
            api_key=os.getenv("ELEVEN_API_KEY"),
            voice="Rachel",
            text=historia
        )
        caminho_arquivo = "/tmp/audio.mp3"
        save(audio, caminho_arquivo)
        print("[OK] Áudio gerado e salvo.")

        # 3. Simular envio por WhatsApp
        numero = os.getenv("WHATSAPP_NUMBER")
        enviar_whatsapp(numero, historia, caminho_arquivo)

        # 4. Registrar na planilha
        adicionar_historico(historia)

        # 5. Enviar por e-mail
        enviar_email("História do dia enviada com sucesso!", historia)

        return {"status": "success"}

    except Exception as e:
        print("[ERRO] Falha ao enviar conto:", e)
        traceback.print_exc()
        return {"status": "error"}
