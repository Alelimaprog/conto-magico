import os
import requests

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = "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"
OPENROUTER_MODEL = "mistralai/mistral-7b-instruct"

def gerar_conto(mensagem_usuario):
    headers = {
        "Authorization": OPENROUTER_API_KEY,  # sem "Bearer"
        "HTTP-Referer": "https://flushimport.com.br",  # seu domínio (ou pode manter esse por enquanto)
        "Content-Type": "application/json"
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": "Você é um contador de histórias infantis"},
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
    except requests.exceptions.RequestException as e:
        print(f"[ERRO DE REDE] {e}")
        return None
    except Exception as e:
        print(f"[ERRO GERAL] {e}")
        return None
