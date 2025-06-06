from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# Inclui todas as rotas definidas em routes.py
app.include_router(router)
