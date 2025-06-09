from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from app.utils import texto_para_audio
import os

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/enviar", response_class=HTMLResponse)
def enviar(request: Request):
    historia = "Era uma vez um macaquinho que queria aprender a voar. Um dia, ele construiu uma asa de folhas e pulou do galho mais alto da floresta. Não voou, mas caiu em cima de um monte de folhas e todos os animais deram risada. A moral da história? Nem sempre vamos voar, mas sempre podemos tentar e nos divertir com o resultado."

    try:
        audio_path = texto_para_audio(historia)
        return FileResponse(audio_path, media_type="audio/mpeg", filename=os.path.basename(audio_path))
    except Exception as e:
        return templates.TemplateResponse("erro.html", {"request": request, "mensagem": str(e)})
