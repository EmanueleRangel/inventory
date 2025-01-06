# app/utils.py
import pandas as pd
import plotly.express as px
from typing import List
from app.models import Item  # ou o modelo que você está utilizando

def generate_graph(items: List[Item]):
    df = pd.DataFrame([{
        "Nome": item.nome,
        "Matrícula": item.matricula,
        "Departamento": item.departamento,
        "Item": item.item_nome
    } for item in items])
    
    fig = px.bar(df, x="Departamento", color="Item", title="Itens por Departamento")
    
    return fig.to_html(full_html=False)
