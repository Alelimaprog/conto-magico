
import os
from elevenlabs.client import ElevenLabs

def enviar_conto_diario(texto, nome_arquivo="conto_audio.mp3"):
    client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

    audio = client.generate(
        text=texto,
        voice="Bella",
        model="eleven_monolingual_v1"
    )

    path = f"/tmp/{nome_arquivo}"
    with open(path, "wb") as f:
        f.write(audio)

    return path
