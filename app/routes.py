from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.utils import texto_para_audio

router = APIRouter()

@router.get("/enviar", response_class=HTMLResponse)
def enviar(request: Request):
    historia = "Era uma vez uma floresta encantada onde os animais falavam e viviam em harmonia..."
    audio_path = texto_para_audio(historia)
    return HTMLResponse(content=f"""
        <html>
        <head><title>História Gerada</title></head>
        <body>
            <h1>História gerada e convertida com sucesso!</h1>
            <audio controls>
                <source src="/static/audio.mp3" type="audio/mpeg">
                Seu navegador não suporta áudio.
            </audio>
        </body>
        </html>
    """)
