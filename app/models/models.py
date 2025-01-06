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

    id = Column(Integer, primary_key=True, index=True)
    matricula = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    departamento = Column(String)
    item_nome = Column(Integer)

class Config:
    orm_mode = True

#class ItemResponse(BaseModel):
 #   id: int
  #  nome: str
   # departamento: str
    #itens: int

    class Config:
        orm_mode = True