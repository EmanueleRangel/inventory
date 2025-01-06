# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco de dados (pode ser modificada para produção ou testes)
SQLALCHEMY_DATABASE_URL = "sqlite:///./inventory.db"  # Altere conforme necessário

# Criação da engine e da sessão
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos
Base = declarative_base()

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()  # Cria uma instância da sessão
    try:
        yield db  # Retorna a sessão para ser usada
    finally:
        db.close()  # Fecha a sessão quando não for mais necessária