from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from app.database import Base, engine # Importando o Base de app.database

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    departamento = Column(String)
    itens = Column(Integer)

    class Config:
        orm_mode = True  # Permite que o Pydantic use o modelo SQLAlchemy

class ItemResponse(BaseModel):
    id: int
    nome: str
    departamento: str
    itens: int

    class Config:
        orm_mode = True

from pydantic import BaseModel

class ItemCreate(BaseModel):
    nome: str
    departamento: str
    itens: int


