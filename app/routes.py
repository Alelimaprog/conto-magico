from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.utils import enviar_mensagem_whatsapp

router = APIRouter()

@router.get("/")
def home():
    html = """
    <html>
        <head>
            <title>Conto Mágico</title>
        </head>
        <body>
            <h1>Conto Mágico</h1>
            <a href='/enviar'>Enviar mensagem</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html)

@router.get("/enviar")
def enviar():
    texto = "📖 História do dia do Conto Mágico! Era uma vez um coelho e uma tartaruga que aprenderam a cooperar..."
    sucesso = enviar_mensagem_whatsapp(texto)
    return HTMLResponse(content="✅ Enviado" if sucesso else "❌ Falhou")
