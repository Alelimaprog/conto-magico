from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/cadastro", response_class=HTMLResponse)
async def cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@router.get("/confirmado", response_class=HTMLResponse)
async def confirmado(request: Request):
    return templates.TemplateResponse("confirmado.html", {"request": request})

@router.get("/painel", response_class=HTMLResponse)
async def painel(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@router.get("/enviar", response_class=HTMLResponse)
async def enviar():
    return HTMLResponse("<h2>Envio funcionando corretamente</h2>")
