# app/models/models.py

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

# Esquema para criação do item (sem ID)
class ItemCreate(BaseModel):
    nome: str
    matricula: str
    departamento: str
    item_nome: str

    class Config:
        orm_mode = True

# Esquema para resposta (com ID)
class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True

# Definição do modelo do SQLAlchemy
class Item:
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    matricula = Column(String)
    departamento = Column(String, index=True)
    item_nome = Column(String)
