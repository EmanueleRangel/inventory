# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
import plotly.express as px

from . import models, database, schemas

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para obter os itens em formato de tabela (JSON)
@app.get("/items/", response_model=list[schemas.ItemResponse])
def get_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

# Rota para visualizar os itens em formato de gráfico
@app.get("/items/graph/", response_class=HTMLResponse)
def get_items_graph(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()

    # Preparando dados para o gráfico
    departamentos = [item.departamento for item in items]
    item_nomes = [item.item_nome for item in items]

    # Criando o gráfico com Plotly
    fig = px.bar(
        x=departamentos, 
        y=item_nomes, 
        labels={'x': 'Departamento', 'y': 'Item'}, 
        title="Distribuição de Itens por Departamento"
    )
    # Converte o gráfico em HTML
    graph_html = fig.to_html(full_html=False)

    return HTMLResponse(content=graph_html)

# Rota para cadastrar um novo item (POST)
@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(nome=item.nome, matricula=item.matricula, departamento=item.departamento, item_nome=item.item_nome)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
