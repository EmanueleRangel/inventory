# models/item.py
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = "itens"
    
    id = Column(Integer, primary_key=True, index=True)
    matricula = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    departamento = Column(String, nullable=False)
    item_nome = Column(String, nullable=False)  # Campo correto para 'item' no banco



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
   
class ItemCreate(BaseModel):
    nome: str
    #matricula = Column(Integer, nullable=False)
    departamento: str
    item_nome: str

class Config:
    orm_mode = True