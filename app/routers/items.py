# app/routers/items.py
from app.models import Item, ItemResponse, ItemCreate  # Corrija os imports
from typing import List
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends
from app import models, schemas
from app.database import SessionLocal  # Corrigindo a importação
from fastapi import APIRouter, Depends
from app.models import Item
from app.utils import generate_graph  # Importando a função generate_graph
from sqlalchemy.orm import Session
from app.database import get_db
from fastapi.responses import HTMLResponse

router = APIRouter()


# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota GET para obter a lista de itens
@router.get("/items/", response_model=list[schemas.ItemResponse])
def get_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

# Rota POST para cadastrar um novo item
@router.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(departamento=item.departamento, itens=item.itens)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/grafico")
def get_graph(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Obtendo todos os itens do banco de dados
    return generate_graph(items)  # Usando a função para gerar o gráfico

@router.get("/grafico", response_class=HTMLResponse)
def get_graph(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Obtendo todos os itens do banco de dados
    return generate_graph(items)  # Retorna o gráfico gerado como HTML

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

