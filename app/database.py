from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Substitua com o caminho correto do banco

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Adie o import para evitar ciclos
def init_db():
    from app.models.models import Item  # Importa apenas quando necessário
    Base.metadata.create_all(bind=engine)
