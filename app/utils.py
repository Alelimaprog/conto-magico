from elevenlabs.client import ElevenLabs
from config.settings import ELEVENLABS_API_KEY

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def enviar_conto_diario(texto, nome_arquivo="conto.mp3"):
    try:
        audio = client.generate(
            text=texto,
            voice="Rachel",
            model="eleven_monolingual_v1"
        )
        client.save(audio, nome_arquivo)
        return True
    except Exception as e:
        print(f"Erro ao gerar áudio: {e}")
        return False