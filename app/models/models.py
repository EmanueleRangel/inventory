from app.database import Base 
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

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

class Item(Base):
    __tablename__ = "items" 

    id = Column(Integer, primary_key=True, autoincrement=True)
    matricula = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    departamento = Column(String, nullable=False)
    item_nome = Column(String, nullable=False)

class ItemCreate(BaseModel):
    nome: str
    matricula = Column(String, nullable=False)
    departamento: str
    itens: int

class Config:
    orm_mode = True