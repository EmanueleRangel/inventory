from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Item, ItemResponse, ItemCreate  # Corrija os imports
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.models import Item, ItemResponse, ItemCreate  # Certifique-se de que os modelos estão corretos
from fastapi.responses import JSONResponse
from fastapi.responses import JSONResponse
from app import models, schemas
from app.models.database import SessionLocal  # Corrigindo a importação
from app.models import Item
from app.utils import generate_graph  # Importando a função generate_graph
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from app.models.database import Base, engine
from app.visualizations import generate_graph

router = APIRouter(prefix="/itens", tags=["Itens"])

@router.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(departamento=item.departamento, itens=item.itens)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
from app.visualizations import generate_graph

router = APIRouter(prefix="/itens", tags=["Itens"])

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
        db_item = Item(**item.dict()) 
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        db.rollback()  # Garante que o banco de dados seja revertido em caso de erro
        raise HTTPException(status_code=500, detail="Error while creating item: " + str(e))

@router.get("/grafico")
def get_graph(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Obtendo todos os itens do banco de dados
    return generate_graph(items)  # Usando a função para gerar o gráfico

@router.get("/grafico", response_class=HTMLResponse)
def get_graph(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Obtendo todos os itens do banco de dados
    return generate_graph(items)  # Retorna o gráfico gerado como HTML

@router.get("/grafico", response_class=JSONResponse)
async def get_graph(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Consulta os itens do banco de dados
    graph_json = generate_graph(items)
    return JSONResponse(content=graph_json)  # Retorna o gráfico como JSON

def main():
    statement = select(Item.items)

if __name__ == "__main__":
    main()
    try:
        items = db.query(Item).all()  # A consulta agora está correta para retornar todos os itens
        if not items:
            raise HTTPException(status_code=404, detail="No items found for graph generation")  # Verifica se há itens
        graph_json = generate_graph(items)  # Gera o gráfico
        #return JSONResponse(content=graph_json)  # conferir erro e ajustar codigo
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error generating graph: " + str(e))

@router.get("/grafico", response_class=HTMLResponse)
def get_graph(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Obtendo todos os itens do banco de dados
    return generate_graph(items) 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()