import os
import requests
from openai import OpenAI

def format_name(name: str) -> str:
    return name.strip().title()

def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email

async def enviar_conto_diario():
    try:
        openai_key = os.getenv("OPENAI_API_KEY")
        eleven_key = os.getenv("ELEVEN_API_KEY")
        twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
        twilio_token = os.getenv("TWILIO_AUTH_TOKEN")
        twilio_number = os.getenv("TWILIO_WHATSAPP_FROM")
        destino = os.getenv("WHATSAPP_NUMBER")

        # 1. Gera uma história curta com OpenAI
        client = OpenAI(api_key=openai_key)
        prompt = (
            "Crie uma história infantil curta e educativa com animais ou crianças como personagens, "
            "de até 3 minutos de leitura, com moral no final. Comece imediatamente com a narrativa."
        )
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        historia = completion.choices[0].message.content.strip()

        # 2. Converte em áudio com ElevenLabs
        voz_id = "EXAVITQu4vr4xnSDxMaL"  # Voz-padrão feminina
        audio_req = requests.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{voz_id}",
            headers={
                "xi-api-key": eleven_key,
                "Content-Type": "application/json"
            },
            json={
                "text": historia,
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.7
                }
            }
        )

        audio_bytes = audio_req.content
        with open("/tmp/audio.mp3", "wb") as f:
            f.write(audio_bytes)

        # 3. Envia texto via WhatsApp
        texto_formatado = f"📚 *Conto Mágico do Dia*\n\n{historia}"
        requests.post(
            "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json".format(twilio_sid),
            auth=(twilio_sid, twilio_token),
            data={
                "From": f"whatsapp:{twilio_number}",
                "To": f"whatsapp:{destino}",
                "Body": texto_formatado
            }
        )

        return True

    except Exception as e:
        print(f"Erro no envio do conto: {e}")
        return False
