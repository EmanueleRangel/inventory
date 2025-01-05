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

router = APIRouter()

# Rota GET para listar os itens
@router.get("/itens", response_model=List[ItemResponse])  # Usando ItemResponse corretamente
async def get_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Consulta os itens no banco de dados
    return items  # Retorna a lista de itens, que será convertida para ItemResponse automaticamente

@router.post("/items/")
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(
        nome=item.nome,
        matricula=item.matricula,
        departamento=item.departamento,
        item_nome=item.item_nome
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/grafico")
def get_graph(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Obtendo todos os itens do banco de dados
    return generate_graph(items)  # Usando a função para gerar o gráfico

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

