from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.models.database import Base  # Garantir que o Base está sendo importado corretamente

DATABASE_URL = "sqlite:///./inventory.db"  # URL do banco de dados

# Criação do engine e sessão
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Verifique se a tabela foi criada
with engine.connect() as connection:
    result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
    tables = result.fetchall()
    print(f"Tabelas no banco de dados: {tables}")
