<<<<<<< HEAD
# app/main.py
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
import plotly.express as px
import pandas as pd
from plotly.io import to_html
from sqlalchemy.orm import Session
from app.models.database import SessionLocal, engine, Base
from app.models import Item
from app.routers import items
from app.models.database import engine
import app.models as models
from app.models import Item
from app.models.database import engine, Base
from app.models.models import Item  # Importe o modelo aqui para criar as tabelas
from app.models.database import get_db
import sys
import os

# Adiciona o diretório raiz ao sys.path para garantir que os módulos sejam encontrados
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from app.models import Item
# Outras importações

app = FastAPI()

Base.metadata.create_all(bind=engine)  # Certifique-se de que as tabelas são criadas

# Inicializando o FastAPI
app = FastAPI()

# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Função para gerar o gráfico
def generate_graph(db: Session):
    # Consulta ao banco de dados
    items = db.query(Item.departamento, Item.itens).all()

    if not items:
        return "<html><body>No data available to display graph</body></html>"

    # Converte os dados para um DataFrame
    df = pd.DataFrame(items, columns=["Departamento", "Itens"])

    # Cria um gráfico de barras
    fig = px.bar(df, x="Departamento", y="Itens", title="Itens por Departamento")
    
    # Converte o gráfico para HTML
    graph_html = to_html(fig, full_html=False)
    return graph_html

# Rota para retornar o gráfico em HTML
@app.get("/grafico", response_class=HTMLResponse)
async def get_graph(db: Session = Depends(get_db)):
    # Gera o gráfico com dados do banco de dados
    graph_html = generate_graph(db)
    return f"<html><body>{graph_html}</body></html>"

# Rota para criar o banco de dados (exemplo)
@app.on_event("startup")
def on_startup():
    # Criação das tabelas
    Base.metadata.create_all(bind=engine)


def create_sample_data(db: Session):
    # Adicionar alguns dados de exemplo, se necessário
    item1 = Item(departamento="TI", itens=10)
    item2 = Item(departamento="RH", itens=20)
    db.add(item1)
    db.add(item2)
    db.commit()

# app/main.py
@app.on_event("startup")
def on_startup():
    # Apaga e recria as tabelas (remova este código se não quiser apagar os dados)
    Base.metadata.drop_all(bind=engine)  # Apaga as tabelas antigas
    Base.metadata.create_all(bind=engine)  # Cria as novas tabelas

# Cria as tabelas no banco de dados ao iniciar a aplicação
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclui as rotas do arquivo de roteadores
app.include_router(items.router)
=======
from fastapi import FastAPI
from app.routers import items
from app.database import Base, engine
import os
import sys
from sqlalchemy import select
#ßfrom app.models import Item

# Exemplo de ajuste no `main.py`
#statement = select(Item)  # Corrige o uso de `Item`


sys.dont_write_bytecode = True

# Adiciona a raiz do projeto ao sys.path (para evitar problemas de importação)
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = FastAPI()

# Inclui as rotas
app.include_router(items.router)

# Cria tabelas no banco de dados
Base.metadata.create_all(bind=engine)
>>>>>>> 6286e90 (remove error from get list and post)
