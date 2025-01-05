# app/main.py

from fastapi import FastAPI
from app.routers import items  # Certifique-se de importar as rotas corretamente

app = FastAPI()

# Registrando as rotas no app FastAPI
app.include_router(items.router)
