# app/main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import plotly.express as px
import pandas as pd
from plotly.io import to_html

app = FastAPI()

# Função para gerar o gráfico
def generate_graph():
    # Simula alguns dados para o gráfico
    df = pd.DataFrame({
        "Departamento": ["TI", "RH", "Vendas", "TI", "Vendas"],
        "Itens": [10, 20, 30, 40, 50]
    })

    # Cria um gráfico de barras
    fig = px.bar(df, x="Departamento", y="Itens", title="Itens por Departamento")
    
    # Converte o gráfico para HTML
    graph_html = to_html(fig, full_html=False)
    return graph_html

# Rota para retornar o gráfico em HTML
@app.get("/grafico", response_class=HTMLResponse)
async def get_graph():
    # Gera o gráfico e retorna como resposta HTML
    graph_html = generate_graph()
    return f"<html><body>{graph_html}</body></html>"
