import os
import requests

OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")

def gerar_conto(mensagem_usuario):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": "Você é um contador de histórias infantis curtas, educativas, criativas e com moral."},
            {"role": "user", "content": mensagem_usuario}
        ]
    }

    try:
        response = requests.post(OPENROUTER_BASE_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        print(f"[ERRO HTTP] {e.response.status_code} - {e.response.text}")
        return None
    except Exception as e:
        print(f"[ERRO] {e}")
        return None
