from app.database import Base 
from sqlalchemy import Column, Integer, String
<<<<<<< HEAD
from .database import Base  # Importe o Base do arquivo database.py
=======
from pydantic import BaseModel
>>>>>>> 446219c (adjust duplicate code)

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

<<<<<<< HEAD
class Item:
>>>>>>> 4d355b0 (remove errors and add improvements)
=======
class Item(Base):
>>>>>>> 6286e90 (remove error from get list and post)
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    departamento = Column(String)
    itens = Column(Integer)

    class Config:
        orm_mode = True  # Permite que o Pydantic use o modelo SQLAlchemy

#class ItemResponse(BaseModel):
 #   id: int
  #  nome: str
   # departamento: str
    #itens: int

    class Config:
<<<<<<< HEAD
        orm_mode = True

from pydantic import BaseModel

class ItemCreate(BaseModel):
    nome: str
    departamento: str
    itens: int


=======
        orm_mode = True
>>>>>>> 446219c (adjust duplicate code)
