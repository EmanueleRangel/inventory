# app/utils.py
import pandas as pd
import plotly.express as px
from typing import List
from app.models import Item  # ou o modelo que você está utilizando

def generate_graph(items: List[Item]):
    # Criar um DataFrame a partir dos itens
    df = pd.DataFrame([{
        "Nome": item.nome,
        "Matrícula": item.matricula,
        "Departamento": item.departamento,
        "Item": item.item_nome
    } for item in items])
    
    # Gerar o gráfico
    fig = px.bar(df, x="Departamento", color="Item", title="Itens por Departamento")
    
    return fig.to_json()  # Retorna o gráfico em formato JSON para ser usado no frontend
