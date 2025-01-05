from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from .database import Base  # Importe o Base do arquivo database.py

<<<<<<< HEAD
class Item(Base):
=======
class ItemCreate(BaseModel):
    nome: str
    matricula: str
    departamento: str
    item_nome: str

    class Config:
        orm_mode = True

class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True

class Item:
>>>>>>> 4d355b0 (remove errors and add improvements)
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


