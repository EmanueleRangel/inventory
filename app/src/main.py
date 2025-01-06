from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
import plotly.express as px
import pandas as pd
from plotly.io import to_html
from sqlalchemy.orm import Session
import app
from app.models.database import SessionLocal, engine, Base
import sys
import os
from app.models.models import Item

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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