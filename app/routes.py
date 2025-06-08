from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from gerador_conto import gerar_conto
from config.twilio import enviar_whatsapp
from config.settings import WHATSAPP_NUMBER

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/enviar", response_class=HTMLResponse)
async def enviar(request: Request):
    conto = gerar_conto("Crie uma história infantil curta com moral positiva.")
    
    if conto:
        sucesso = enviar_whatsapp(WHATSAPP_NUMBER, conto)
        if not sucesso:
            conto = "Erro ao enviar mensagem via WhatsApp."

    return templates.TemplateResponse("enviar.html", {"request": request, "conto": conto})
