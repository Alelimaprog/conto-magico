import os
import requests

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = "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"
OPENROUTER_MODEL = "mistralai/mistral-7b-instruct"

def gerar_conto(mensagem_usuario):
    session = requests.Session()
    request = requests.Request(
        method="POST",
        url=OPENROUTER_BASE_URL,
        headers={
            "Authorization": OPENROUTER_API_KEY,  # Sem Bearer
            "HTTP-Referer": "https://flushimport.com.br",  # Qualquer domínio válido
            "Content-Type": "application/json"
        },
        json={
            "model": OPENROUTER_MODEL,
            "messages": [
                {"role": "system", "content": "Você é um contador de histórias infantis"},
                {"role": "user", "content": mensagem_usuario}
            ]
        }
    )

    prepared = request.prepare()

    try:
        response = session.send(prepared)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        print(f"[ERRO HTTP] {e.response.status_code} - {e.response.text}")
    except Exception as e:
        print(f"[ERRO GERAL] {e}")
        if response:
            print(response.text)
