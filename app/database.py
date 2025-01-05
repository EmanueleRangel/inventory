# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL  # Ajuste se necessário

# Configuração do banco de dados
SQLALCHEMY_DATABASE_URL = DATABASE_URL  # Exemplo: 'sqlite:///./test.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Função get_db
def get_db():
    db = SessionLocal()  # Cria uma nova sessão
    try:
        yield db  # Retorna a sessão para ser usada nas rotas
    finally:
        db.close()  # Fecha a sessão após a execução
