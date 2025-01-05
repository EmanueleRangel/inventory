# app/routers/items.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Item, ItemResponse, ItemCreate  # Corrija os imports
from app.database import get_db
from typing import List
from fastapi.responses import JSONResponse
from app.models import Item, ItemResponse, ItemCreate 


router = APIRouter()

# Rota GET para listar os itens
@router.get("/itens", response_model=List[ItemResponse])  # Usando ItemResponse corretamente
async def get_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Consulta os itens no banco de dados
    return items  # Retorna a lista de itens, que será convertida para ItemResponse automaticamente

# Rota POST para cadastrar um novo item
@router.post("/itens", response_model=ItemResponse)  # Usando ItemResponse corretamente
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())  # Converte o modelo Pydantic para SQLAlchemy
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item  # Retorna o item criado, usando o modelo ItemResponse para formatação

# Rota GET para gerar gráfico
@router.get("/grafico", response_class=JSONResponse)
async def get_graph(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Consulta os itens do banco de dados
    graph_json = generate_graph(items)
    return JSONResponse(content=graph_json)  # Retorna o gráfico como JSON
