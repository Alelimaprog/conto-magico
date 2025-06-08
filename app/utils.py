import requests
from config.settings import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL

def gerar_conto(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": "Você é um contador de histórias infantis curtas, com uma moral no final."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(OPENROUTER_BASE_URL, headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"OpenRouter falhou: {response.status_code} {response.text}")

    result = response.json()
    return result["choices"][0]["message"]["content"]
