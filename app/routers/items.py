from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Item
from app.schemas import ItemCreate, ItemResponse
from typing import List

router = APIRouter()

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar um novo item
@router.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(nome=item.nome, matricula=item.matricula, departamento=item.departamento, item_nome=item.item_nome)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Rota para listar todos os itens
@router.get("/items/", response_model=List[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items
