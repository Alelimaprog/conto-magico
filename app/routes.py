from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from app.utils import enviar_conto_diario

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/enviar", response_class=JSONResponse)
async def enviar():
    sucesso = enviar_conto_diario()
    return {"status": "ok" if sucesso else "erro"}
from teste_whatsapp import router as teste_router
router.include_router(teste_router)
