import plotly.express as px
import pandas as pd
from typing import List
from ..models.models import Item

def generate_graph(items: List[Item]):
    df = pd.DataFrame([{
        "Nome": item.nome,
        "Matrícula": item.matricula,
        "Departamento": item.departamento,
        "Item": item.item_nome
    } for item in items])
    
    fig = px.bar(df, x="Departamento", color="Item", title="Itens por Departamento")
    
    return fig.to_json()
