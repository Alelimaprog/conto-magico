import os
from config.twilio import enviar_whatsapp

# Garante que variáveis estejam carregadas (se estiver em .env local)
from dotenv import load_dotenv
load_dotenv()

# Recupera o número do destinatário
numero = os.getenv("WHATSAPP_NUMBER")
mensagem = "Mensagem de teste do Conto Mágico"

# Chama função de envio
enviado = enviar_whatsapp(numero, mensagem)

print("[OK] Enviado" if enviado else "[ERRO] Falhou ao enviar")
