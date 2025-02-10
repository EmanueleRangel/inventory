from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from src.models.database import Base

DATABASE_URL = "sqlite:///./inventory.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

with engine.connect() as connection:
    result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
    tables = result.fetchall()
    print(f"Tabelas no banco de dados: {tables}")
