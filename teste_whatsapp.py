from fastapi import APIRouter
import os
from config.twilio import enviar_whatsapp

router = APIRouter()

@router.get("/teste-whatsapp")
def testar_envio():
    numero = os.getenv("WHATSAPP_NUMBER")
    mensagem = "Mensagem de teste do Conto Mágico via rota HTTP"
    status = enviar_whatsapp(numero, mensagem)
    return {"status": "ok" if status else "erro"}
