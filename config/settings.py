import os

# 🔐 ElevenLabs
ELEVENLABS_API_KEY = os.getenv("ELEVEN_API_KEY", "sk_eee82b6166601c7cf13d5345b0671f0e424956a78715137")

# 📬 E-mail de envio
EMAIL_ORIGEM = os.getenv("EMAIL_ORIGEM", "importusabraz@gmail.com")
EMAIL_SENHA = os.getenv("EMAIL_SENHA", "")

# 💳 MercadoPago
MERCADOPAGO_ACCESS_TOKEN = os.getenv("MERCADOPAGO_ACCESS_TOKEN", "")

# 🤖 OpenRouter (modelo de IA)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "")

# 📊 Planilha Google (ID)
PLANILHA_ID = os.getenv("PLANILHA_ID", "")

# 📞 Twilio WhatsApp
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
TWILIO_WHATSAPP = os.getenv("TWILIO_WHATSAPP", "whatsapp:+14155238886")  # padrão do sandbox
