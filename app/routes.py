from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.utils import enviar_conto_diario

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/cadastro", response_class=HTMLResponse)
def cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@router.post("/cadastro")
async def processar_cadastro(request: Request, telefone: str = Form(...)):
    await enviar_conto_diario(telefone)
    return templates.TemplateResponse("confirmado.html", {"request": request})

@router.get("/enviar", response_class=HTMLResponse)
def enviar(request: Request):
    return templates.TemplateResponse("confirmado.html", {"request": request})
