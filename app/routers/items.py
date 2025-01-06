from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.models import Item, ItemResponse, ItemCreate  # Certifique-se de que os modelos estão corretos
from app.database import get_db
from fastapi.responses import JSONResponse
from app.visualizations import generate_graph

router = APIRouter(prefix="/itens", tags=["Itens"])

# Rota GET para listar todos os itens
@router.get("/", response_model=List[ItemResponse])  # Especifica o tipo de resposta como lista de itens
async def get_items(db: Session = Depends(get_db)):
    try:
        items = db.query(Item).all()  # A consulta deve retornar todos os itens corretamente
        if not items:
            raise HTTPException(status_code=404, detail="No items found")  # Retorna 404 se não encontrar itens
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Trata possíveis erros da consulta

# Rota POST para criar um novo item
@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    try:
        db_item = Item(**item.dict())  # Converte o modelo Pydantic para SQLAlchemy
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item  # Retorna o item criado, formatado como ItemResponse
    except Exception as e:
        db.rollback()  # Garante que o banco de dados seja revertido em caso de erro
        raise HTTPException(status_code=500, detail="Error while creating item: " + str(e))

# Rota GET para gerar gráfico
@router.get("/grafico", response_class=JSONResponse)
async def get_graph(db: Session = Depends(get_db)):
    try:
        items = db.query(Item).all()  # A consulta agora está correta para retornar todos os itens
        if not items:
            raise HTTPException(status_code=404, detail="No items found for graph generation")  # Verifica se há itens
        graph_json = generate_graph(items)  # Gera o gráfico
        return JSONResponse(content=graph_json)  # Retorna o gráfico como JSON
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error generating graph: " + str(e))
