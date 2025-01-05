# app/main.py

from fastapi import FastAPI
from app.routers import items  # Importando as rotas do arquivo items.py

app = FastAPI()

# Registrando as rotas no app FastAPI
app.include_router(items.router)
