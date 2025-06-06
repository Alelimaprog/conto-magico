from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/painel", response_class=HTMLResponse)
def painel(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@router.get("/cadastro", response_class=HTMLResponse)
def cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@router.get("/admin", response_class=HTMLResponse)
def admin(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})