# app/models.py

from pydantic import BaseModel

# Modelo Pydantic para resposta de Item
class ItemBase(BaseModel):
    nome: str
    matricula: str
    departamento: str
    item_nome: str

    class Config:
        orm_mode = True  # Permite que o Pydantic trabalhe com objetos SQLAlchemy

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
