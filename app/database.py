from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados (use o URL correto do seu banco de dados)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Para SQLite, ou outro banco de dados

# Cria o engine de conexão
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  # Necessário para SQLite

# Cria a sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para as classes de modelos
Base = declarative_base()

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
