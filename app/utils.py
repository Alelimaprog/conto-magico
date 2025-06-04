from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

resposta = client.chat.completions.create(
    model="mistral/mistral-7b-instruct",
    messages=[{"role": "user", "content": prompt}]
)
