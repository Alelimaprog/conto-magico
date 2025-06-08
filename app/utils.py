import os
import requests
import traceback

from config.twilio import enviar_whatsapp
from config.planilha import adicionar_historico
from config.email import enviar_email

try:
    from elevenlabs import generate, save
    ELEVENLABS_OK = True
except ImportError:
    ELEVENLABS_OK = False

def enviar_conto_diario():
    try:
        # 1. Gerar história com OpenRouter (GPT)
        url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1/chat/completions")
        headers = {
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json",
            "X-Title": "Conto Magico"
        }
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": "Crie uma história infantil curta (até 3 minutos), com moral educativa e personagens animais."
                }
            ]
        }

        resposta = requests.post(url, headers=headers, json=data)

        if not resposta.ok:
            print("[ERRO] OpenRouter falhou:", resposta.status_code, resposta.text)
            return {"status": "erro_openrouter"}

        historia = resposta.json()["choices"][0]["message"]["content"].strip()
        print("[OK] História gerada.")

        numero = os.getenv("WHATSAPP_NUMBER")

        # 2. Tenta gerar e enviar o áudio se possível
        caminho_arquivo = None
        if ELEVENLABS_OK:
            try:
                audio = generate(
                    api_key=os.getenv("ELEVENLABS_API_KEY"),
                    voice="OB6x7EbXYlhG4DDTB1XU",  # Voz PT-BR infantil
                    text=historia
                )
                caminho_arquivo = "static/audio.mp3"
                save(audio, caminho_arquivo)
                print("[OK] Áudio gerado.")
            except Exception as e:
                print("[AVISO] Falha ao gerar/enviar áudio. Segue com texto apenas.")
                caminho_arquivo = None

        # 3. Envia WhatsApp (com ou sem áudio)
        enviado = enviar_whatsapp(numero, historia, caminho_arquivo)
        print("[OK] WhatsApp enviado.")

        # 4. Histórico e e-mail simulados
        adicionar_historico(historia)
        print("[OK] Histórico salvo.")

        enviar_email("História do dia enviada com sucesso!", historia)
        print("[OK] E-mail enviado.")

        return {"status": "success"}

    except Exception as e:
        print("[ERRO] Falha ao enviar conto:", e)
        traceback.print_exc()
        return {"status": "error"}
