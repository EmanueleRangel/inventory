from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.models.database import get_db
from app.models.models import Item

# Obtenha uma instância da sessão
db = next(get_db())

# Agora você pode usar `db` para consultas
result = db.query(Item).filter(Item.some_column == 'valor_especifico').all()


DATABASE_URL = "sqlite:///./test.db"  # Substitua pela URL do seu banco de dados

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependência para obter a sessão do banco de dados
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
