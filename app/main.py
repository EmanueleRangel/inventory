from fastapi import FastAPI
from app.models.database import Base, engine, SessionLocal
from app.models.models import Item
from app.routers import graph

# Criar a instância da aplicação
app = FastAPI()

# Criação das tabelas e dados de exemplo
@app.on_event("startup")
def on_startup():
    Base.metadata.drop_all(bind=engine)  # Apaga as tabelas antigas
    Base.metadata.create_all(bind=engine)  # Cria as novas tabelas
    with SessionLocal() as session:
        session.add_all([
            Item(departamento="TI", itens=10),
            Item(departamento="RH", itens=20),
            Item(departamento="Financeiro", itens=15),
        ])
        session.commit()

# Inclui o roteador de gráficos
app.include_router(graph.router)
