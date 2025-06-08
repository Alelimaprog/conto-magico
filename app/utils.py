import os
import requests
from app.settings import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL

def enviar_conto_diario():
    url = OPENROUTER_BASE_URL
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "Você é um contador de histórias infantis curtas, educativas, criativas e com moral."
            },
            {
                "role": "user",
                "content": "Crie uma história infantil curta com moral positiva."
            }
        ]
    }

    resposta = requests.post(url, headers=headers, json=payload)

    print("[DEBUG] OpenRouter status:", resposta.status_code)
    print("[DEBUG] OpenRouter body:", resposta.text)

    resposta.raise_for_status()
    return resposta.json()
