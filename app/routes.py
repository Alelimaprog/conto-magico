from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.utils import gerar_conto
from app.whatsapp import enviar_mensagem_whatsapp

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/enviar", response_class=HTMLResponse)
def enviar_mensagem(request: Request):
    try:
        historia = gerar_conto()
        texto = f"📖 História do dia do Conto Mágico!

{historia}"
        enviar_mensagem_whatsapp(texto)
        return templates.TemplateResponse("resultado.html", {"request": request, "mensagem": "Enviado com sucesso!"})
    except Exception as e:
        print(f"[ERRO /enviar] {e}")
        return templates.TemplateResponse("erro.html", {"request": request, "mensagem": "Erro ao gerar história."})
