from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.utils import texto_para_audio
import os

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/enviar", response_class=HTMLResponse)
def enviar(request: Request):
    historia = "Era uma vez uma menina que adorava ouvir histórias mágicas antes de dormir."
    audio_path = texto_para_audio(historia)
    return templates.TemplateResponse("enviado.html", {"request": request, "audio_path": audio_path})
