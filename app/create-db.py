from app.database import Base, engine
from app.models import Item

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)
