from fastapi import FastAPI
from app.routers import items  # Certifique-se de que o caminho da importação esteja correto

app = FastAPI()

# Incluindo o router de itens
app.include_router(items.router)
