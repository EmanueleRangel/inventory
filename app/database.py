# app/models/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco de dados
DATABASE_URL = "sqlite:///./test.db"  # Ajuste para o seu banco de dados

# Criação do engine e sessão
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação do Base para SQLAlchemy
Base = declarative_base()
