from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
import plotly.express as px
import pandas as pd
from plotly.io import to_html
from sqlalchemy.orm import Session
import app
from app import models
from app.models.database import SessionLocal, engine, Base
import sys
import os
from app.models.models import Item
from app.routers import items

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

session = get_session() # type: ignore

def main():
    print("Olá, mundo! Este é o meu novo projeto.")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = FastAPI()

Base.metadata.create_all(bind=engine)  # Certifique-se de que as tabelas são criadas

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # Criação das tabelas
    Base.metadata.create_all(bind=engine)


def create_sample_data(db: Session):
    # Adicionar alguns dados de exemplo, se necessário
    item1 = Item(departamento="TI", itens=10)
    item2 = Item(departamento="RH", itens=20)
    db.add(item1)
    db.add(item2)
    db.commit()

@app.on_event("startup")
def on_startup():
    Base.metadata.drop_all(bind=engine)  # Apaga as tabelas antigas
    Base.metadata.create_all(bind=engine)  # Cria as novas tabelas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router)