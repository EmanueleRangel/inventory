# app/schemas.py
from pydantic import BaseModel

# Esquema para criação do item (sem ID)
class ItemCreate(BaseModel):
    nome: str
    matricula: str
    departamento: str
    item_nome: str

    class Config:
        orm_mode = True  # Permite a conversão de objetos SQLAlchemy para dict

# Esquema para resposta (com ID)
class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True
