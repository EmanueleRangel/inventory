from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Aqui você coloca a URL de conexão com o banco de dados (ajuste conforme necessário)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Usando SQLite, pode ser substituído por qualquer banco de sua escolha

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  # Para SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
