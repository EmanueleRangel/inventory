# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Configuração do banco de dados (SQLite por padrão)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Altere conforme necessário

# Criação da engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos
Base = declarative_base()

# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados
engine = create_engine('sqlite:///:memory:')  # Substitua pelo URL do seu banco de dados real
Session = sessionmaker(bind=engine)

def get_session():
    return Session()


# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
