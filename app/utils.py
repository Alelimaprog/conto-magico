import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")

def gerar_conto():
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "Você é um contador de histórias infantis criativas, educativas e com moral."
            },
            {
                "role": "user",
                "content": "Crie uma história infantil completa, com começo, meio e fim, incluindo uma moral no final."
            }
        ]
    }

    try:
        resposta = requests.post(OPENROUTER_BASE_URL, headers=headers, json=payload)
        resposta.raise_for_status()
        return resposta.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"[ERRO gerar_conto] {e}")
        raise
