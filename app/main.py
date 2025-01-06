from fastapi import FastAPI
from app.routers import items
from app.database import Base, engine
import os
import sys
from sqlalchemy import select
#ßfrom app.models import Item

# Exemplo de ajuste no `main.py`
#statement = select(Item)  # Corrige o uso de `Item`


sys.dont_write_bytecode = True

# Adiciona a raiz do projeto ao sys.path (para evitar problemas de importação)
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = FastAPI()

# Inclui as rotas
app.include_router(items.router)

# Cria tabelas no banco de dados
Base.metadata.create_all(bind=engine)
