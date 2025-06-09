from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.utils import enviar_mensagem_whatsapp, texto_para_audio
import os
import requests

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")

def gerar_conto():
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": "Você é um contador de histórias infantis criativas, educativas e com moral positiva."},
            {"role": "user", "content": "Crie uma história infantil curta e divertida com uma moral no final."}
        ]
    }
    try:
        response = requests.post(OPENROUTER_BASE_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"[ERRO gerar_conto] {e}")
        return None

@router.get("/enviar", response_class=HTMLResponse)
def enviar(request: Request):
    historia = gerar_conto()
    if not historia:
        return templates.TemplateResponse("erro.html", {"request": request, "mensagem": "Erro ao gerar história."})

    audio_path = texto_para_audio(historia)
    sucesso = enviar_mensagem_whatsapp(audio_path, tipo="audio")

    if sucesso:
        return templates.TemplateResponse("enviado.html", {"request": request})
    else:
        return templates.TemplateResponse("erro.html", {"request": request, "mensagem": "Erro ao enviar mensagem."})
