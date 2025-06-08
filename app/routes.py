from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.utils import gerar_conto, enviar_mensagem_whatsapp

router = APIRouter()

@router.get("/")
def home():
    html = """
    <html>
        <head><title>Conto Mágico</title></head>
        <body>
            <h1>Conto Mágico</h1>
            <a href='/enviar'>Enviar história</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html)

@router.get("/enviar")
def enviar():
    prompt = "Crie uma história infantil curta, educativa, criativa e com uma moral positiva no final."
    historia = gerar_conto(prompt)
    if not historia:
        return HTMLResponse(content="❌ Erro ao gerar história.")
    
    sucesso = enviar_mensagem_whatsapp("📖 História do dia do Conto Mágico:\n\n" + historia)
    return HTMLResponse(content="✅ Enviado" if sucesso else "❌ Falha ao enviar no WhatsApp")
