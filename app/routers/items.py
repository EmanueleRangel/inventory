# app/routers/items.py
<<<<<<< HEAD
=======
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
>>>>>>> 4d355b0 (remove errors and add improvements)
from app.models import Item, ItemResponse, ItemCreate  # Corrija os imports
from typing import List
from fastapi.responses import JSONResponse
<<<<<<< HEAD
from fastapi import APIRouter, Depends
from app import models, schemas
from app.models.database import SessionLocal  # Corrigindo a importação
from fastapi import APIRouter, Depends
from app.models import Item
from app.utils import generate_graph  # Importando a função generate_graph
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from app.models.database import Base, engine
from app.models.database import get_db
=======
from app.models import Item, ItemCreate, ItemResponse
from app.visualizations import generate_graph

>>>>>>> 4d355b0 (remove errors and add improvements)

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

<<<<<<< HEAD
=======
# Rota GET para gerar gráfico
@router.get("/grafico", response_class=JSONResponse)
async def get_graph(db: Session = Depends(get_db)):
    items = db.query(Item).all()  # Consulta os itens do banco de dados
    graph_json = generate_graph(items)
    return JSONResponse(content=graph_json)  # Retorna o gráfico como JSON


def main():
    statement = select(Item.items)

if __name__ == "__main__":
    main()
>>>>>>> 4d355b0 (remove errors and add improvements)
