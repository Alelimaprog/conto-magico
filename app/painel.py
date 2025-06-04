from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import sqlite3
from config.twilio import enviar_whatsapp

painel_router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Cria o banco se não existir
def init_db():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            ativo INTEGER DEFAULT 1
        )
    """)
    conn.commit()
    conn.close()

init_db()

@painel_router.get("/painel", response_class=HTMLResponse)
async def painel_admin(request: Request):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return templates.TemplateResponse("admin.html", {"request": request, "usuarios": usuarios})

@painel_router.get("/cadastro", response_class=HTMLResponse)
async def formulario_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@painel_router.post("/cadastro")
async def salvar_usuario(nome: str = Form(...), telefone: str = Form(...)):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, telefone) VALUES (?, ?)", (nome, telefone))
    conn.commit()
    conn.close()

    # Enviar mensagem automática
    mensagem = "👋 Olá! Você foi cadastrado com sucesso no *Conto Mágico*. Em breve começará a receber histórias incríveis no seu WhatsApp!"
    enviar_whatsapp(telefone, mensagem)

    return RedirectResponse("/confirmado", status_code=303)

@painel_router.get("/confirmado", response_class=HTMLResponse)
async def confirmado(request: Request):
    return templates.TemplateResponse("confirmado.html", {"request": request})

@painel_router.get("/remover/{usuario_id}")
async def remover_usuario(usuario_id: int):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT telefone FROM usuarios WHERE id=?", (usuario_id,))
    telefone_removido = cursor.fetchone()

    cursor.execute("DELETE FROM usuarios WHERE id=?", (usuario_id,))
    conn.commit()
    conn.close()

    # Enviar mensagem de remoção
    if telefone_removido:
        mensagem = "⚠️ Você foi removido do *Conto Mágico*. Se foi um engano, entre em contato conosco!"
        enviar_whatsapp(telefone_removido[0], mensagem)

    return RedirectResponse("/painel", status_code=303)
