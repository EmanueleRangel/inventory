from fastapi import FastAPI
from app.routers import items  # Importe as rotas

app = FastAPI()

# Incluindo o router de itens
app.include_router(items.router)
