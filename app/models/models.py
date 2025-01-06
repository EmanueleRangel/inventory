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
    __tablename__ = "items"  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, autoincrement=True)  # Definindo 'id' como autoincremento
    matricula = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    departamento = Column(String, nullable=False)
    item_nome = Column(String, nullable=False)

class Config:
    orm_mode = True

#class ItemResponse(BaseModel):
 #   id: int
  #  nome: str
   # departamento: str
    #itens: int

    class Config:
        orm_mode = True