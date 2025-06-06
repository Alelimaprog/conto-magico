from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.utils import enviar_conto_diario

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/cadastro", response_class=HTMLResponse)
async def exibir_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@router.post("/cadastro", response_class=HTMLResponse)
async def processar_cadastro(request: Request, nome: str = Form(...), telefone: str = Form(...)):
    # Aqui o cadastro seria salvo em planilha ou banco
    return templates.TemplateResponse("confirmado.html", {"request": request})

@router.get("/painel", response_class=HTMLResponse)
async def painel_admin(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@router.get("/admin", response_class=HTMLResponse)
async def admin_redirect(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@router.get("/enviar", response_class=HTMLResponse)
async def enviar(request: Request):
    try:
        enviar_conto_diario()
        return templates.TemplateResponse("confirmado.html", {"request": request})
    except Exception as e:
        return HTMLResponse(content=f"Erro ao enviar: {e}", status_code=500)