# app/models/models.py
from pydantic import BaseModel

# app/models/models.py
from sqlalchemy import Column, Integer, String
from app.database import Base  # Certifique-se de que o Base está sendo importado corretamente

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    matricula = Column(String)
    departamento = Column(String)
    item_nome = Column(String)

    def __repr__(self):
        return f"<Item(nome={self.nome}, matricula={self.matricula}, departamento={self.departamento}, item_nome={self.item_nome})>"


class ItemCreate(BaseModel):
    nome: str
    matricula: str
    departamento: str
    item_nome: str

    class Config:
        orm_mode = True  # Permite que o Pydantic converta para o modelo SQLAlchemy

class ItemResponse(ItemCreate):
    id: int  # Adiciona o campo 'id' para a resposta

    class Config:
        orm_mode = True  # Permite que o Pydantic converta para o modelo SQLAlchemy
