from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.utils import enviar_mensagem_whatsapp
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

    prompt = (
        "Crie uma história infantil curta, divertida e com uma moral positiva no final. "
        "A história deve ter no máximo 3 parágrafos."
    )

    payload = {
        "model": OPENROUTER_MODEL,
        "prompt": prompt,
        "max_tokens": 500,
        "temperature": 0.9
    }

    try:
        response = requests.post(OPENROUTER_BASE_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["text"].strip()
    except Exception as e:
        print(f"[ERRO gerar_conto] {e}")
        return None

@router.get("/enviar", response_class=HTMLResponse)
def enviar(request: Request):
    historia = gerar_conto()
    if not historia:
        return templates.TemplateResponse("erro.html", {"request": request, "mensagem": "Erro ao gerar história."})

    texto = f"📖 História do dia do Conto Mágico!\n\n{historia}"

    sucesso = enviar_mensagem_whatsapp(texto)
    if sucesso:
        return templates.TemplateResponse("enviado.html", {"request": request})
    else:
        return templates.TemplateResponse("erro.html", {"request": request, "mensagem": "Erro ao enviar mensagem."})
