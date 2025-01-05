# app/models.py

from pydantic import BaseModel

# Modelo Pydantic base para Item
class ItemBase(BaseModel):
    nome: str
    matricula: str
    departamento: str
    item_nome: str

    class Config:
        orm_mode = True  # Permite que Pydantic converta objetos SQLAlchemy em modelos Pydantic

# Modelo para criação de item
class ItemCreate(ItemBase):
    pass

# Modelo para resposta de item, com o ID
class ItemResponse(ItemBase):
    id: int
