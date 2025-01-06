from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
import plotly.express as px
import pandas as pd
from plotly.io import to_html
from sqlalchemy.orm import Session
from app.models.database import SessionLocal, engine, Base #get_db
from app.routers import items
import app.models as models
from app.models.database import SessionLocal, engine, Base
from app.models import Item
from app.models.database import SessionLocal, engine, Base #get_db
from app.routers import items
from app.models.database import engine
import app.models as models
from app.models import Item
from app.models.database import engine, Base
from app.models.models import Item 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = FastAPI()

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_graph(db: Session):
    items = db.query(Item.departamento, Item.itens).all()

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
    item1 = Item(departamento="TI", itens=10)
    item2 = Item(departamento="RH", itens=20)
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