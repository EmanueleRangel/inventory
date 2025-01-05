# app/routers/items.py
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.models import Item
from app.database import get_db
import pandas as pd
import plotly.express as px
from typing import List

router = APIRouter()

@router.get("/itens", response_model=List[ItemResponse])  # Use o modelo Pydantic
async def get_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Consulta os itens no banco de dados
    return items  # Retorna a lista de itens

@router.post("/itens", response_model=ItemResponse)  # Use o modelo Pydantic
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())  # Converte o modelo Pydantic para SQLAlchemy
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item  # Retorna o item criado, usando o modelo Pydantic

router = APIRouter()
def generate_graph(items: List[Item]):
    df = pd.DataFrame([{
        "Nome": item.nome,
        "Matrícula": item.matricula,
        "Departamento": item.departamento,
        "Item": item.item_nome
    } for item in items])
    
    fig = px.bar(df, x="Departamento", color="Item", title="Itens por Departamento")
    return fig.to_json()

@router.get("/grafico", response_class=JSONResponse)
async def get_graph(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Consulta os itens do banco de dados
    graph_json = generate_graph(items)
    return JSONResponse(content=graph_json)  # Retorna o gráfico como JSON