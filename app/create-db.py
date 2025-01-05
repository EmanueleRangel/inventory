from app.database import engine
from app.models import Item

# Criar as tabelas no banco de dados
Item.metadata.create_all(bind=engine)
