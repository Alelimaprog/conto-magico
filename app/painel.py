from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sqlite3

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

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

@app.get("/painel", response_class=HTMLResponse)
async def painel_admin(request: Request):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return templates.TemplateResponse("admin.html", {"request": request, "usuarios": usuarios})

@app.get("/cadastro", response_class=HTMLResponse)
async def formulario_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.post("/cadastro")
async def salvar_usuario(nome: str = Form(...), telefone: str = Form(...)):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, telefone) VALUES (?, ?)", (nome, telefone))
    conn.commit()
    conn.close()
    return RedirectResponse("/confirmado", status_code=303)

@app.get("/confirmado", response_class=HTMLResponse)
async def confirmado(request: Request):
    return templates.TemplateResponse("confirmado.html", {"request": request})

@app.get("/remover/{usuario_id}")
async def remover_usuario(usuario_id: int):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=?", (usuario_id,))
    conn.commit()
    conn.close()
    return RedirectResponse("/painel", status_code=303)
