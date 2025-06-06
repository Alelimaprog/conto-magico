import os

# Configurações de autenticação de e-mail
EMAIL_ORIGEM = os.getenv("EMAIL_ORIGEM")
EMAIL_SENHA = os.getenv("EMAIL_SENHA")

# Chaves de API externas
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")  # 🔧 Corrigido aqui

# Integração com Google Sheets
PLANILHA_ID = os.getenv("PLANILHA_ID")

# Integração com Mercado Pago
MERCADOPAGO_ACCESS_TOKEN = os.getenv("MERCADOPAGO_ACCESS_TOKEN")
