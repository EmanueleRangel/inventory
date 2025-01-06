import plotly.express as px
import pandas as pd
from typing import List
from app.models.models import Item
import sys
import os
from sqlalchemy.orm import Session
from app.models.models import Item

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def generate_graph(items: List[Item]):
    df = pd.DataFrame([{
        "Nome": item.nome,
        "Matrícula": item.matricula,
        "Departamento": item.departamento,
        "Item": item.item_nome
    } for item in items])
    
    fig = px.bar(df, x="Departamento", color="Item", title="Itens por Departamento")
    
    return fig.to_json()

def generate_graph(db: Session):
    items = db.query(Item).all()  # Consulta válida
    # Lógica para gerar gráficos com os dados de `items`