from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.models.database import get_session
from app.models.models import Item
import plotly.express as px
import pandas as pd
from plotly.io import to_html

router = APIRouter()

# Função para gerar o gráfico
def generate_graph(db: Session):
    items = db.query(Item.departamento, Item.itens).all()
    if not items:
        return "<html><body>No data available</body></html>"

    df = pd.DataFrame(items, columns=["Departamento", "Itens"])
    fig = px.bar(df, x="Departamento", y="Itens", title="Itens por Departamento")
    return to_html(fig, full_html=False)

# Rota para exibir o gráfico
@router.get("/grafico", response_class=HTMLResponse)
async def get_graph(db: Session = Depends(get_session)):
    graph_html = generate_graph(db)
    return f"<html><body>{graph_html}</body></html>"
