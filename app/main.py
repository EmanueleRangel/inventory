from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
import plotly.express as px
import pandas as pd
from plotly.io import to_html
from app.routers import items
from app.models.database import SessionLocal, engine, Base
from app.models.database import engine
import app.models as models
from app.models import Item, ItemCreate, ItemResponse 
from app.models.models import Item 
import sys
import os
from sqlalchemy.orm import Session
from app.models.database import engine, Base

# Evento de inicialização
@app.on_event("startup") # type: ignore
def on_startup():
    # Deleta as tabelas se já existirem (não recomendado para produção)
    Base.metadata.drop_all(bind=engine)  # Apaga as tabelas antigas
    Base.metadata.create_all(bind=engine)  # Cria as novas tabelas


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())  # Passando os dados do Pydantic para o modelo SQLAlchemy
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = FastAPI()

Base.metadata.create_all(bind=engine)

app = FastAPI()



def generate_graph(db: Session):
    items = db.query(Item.departamento, Item.item_nome).all()

    if not items:
        return "<html><body>No data available to display graph</body></html>"

    df = pd.DataFrame(items, columns=["Departamento", "Itens"])

    fig = px.bar(df, x="Departamento", y="Itens", title="Itens por Departamento")
    
    graph_html = to_html(fig, full_html=False)
    return graph_html

@app.get("/grafico", response_class=HTMLResponse)
async def get_graph(db: Session = Depends(get_db)):
    graph_html = generate_graph(db)
    return f"<html><body>{graph_html}</body></html>"

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


def create_sample_data(db: Session):
    item1 = Item(departamento="TI", item_nome=10)
    item2 = Item(departamento="RH", item_nome=20)
    db.add(item1)
    db.add(item2)
    db.commit()

# app/main.py
@app.on_event("startup")
def on_startup():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine) 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

sys.dont_write_bytecode = True

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = FastAPI()

app.include_router(items.router)

sys.dont_write_bytecode = True

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = FastAPI()

app.include_router(items.router)

Base.metadata.create_all(bind=engine)