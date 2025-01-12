from app.models.database import engine
from app.models import Items

# Criar as tabelas no banco de dados
Items.metadata.create_all(bind=engine)
