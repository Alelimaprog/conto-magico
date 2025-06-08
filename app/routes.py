from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.utils import enviar_mensagem_whatsapp
from gerador_conto import gerar_conto

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>Conto Mágico</title>
            <style>
                body { font-family: Arial, sans-serif; }
                .topo { background: #4CAF50; padding: 20px; color: white; font-size: 24px; }
                .conteudo { padding: 20px; }
            </style>
        </head>
        <body>
            <div class="topo">Conto Mágico</div>
            <div class="conteudo">
                <p><a href="/enviar">Clique aqui para enviar uma história de teste</a></p>
            </div>
        </body>
    </html>
    """

@router.get("/enviar", response_class=HTMLResponse)
async def enviar():
    prompt = "Crie uma história infantil curta sobre amizade e respeito com uma moral positiva no final."
    historia = gerar_conto(prompt)

    if not historia:
        return HTMLResponse(content="<h3 style='color:red'>❌ Erro ao gerar história.</h3>", status_code=500)

    mensagem = f"📖 História do dia do Conto Mágico!\n\n{historia.strip()}"

    enviado = enviar_mensagem_whatsapp(mensagem)
    if enviado:
        return HTMLResponse(content="<h3 style='color:green'>✅ Enviado com sucesso!</h3>")
    else:
        return HTMLResponse(content="<h3 style='color:red'>❌ Erro ao enviar mensagem.</h3>", status_code=500)
