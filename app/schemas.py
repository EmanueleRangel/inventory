# app/schemas.py
from pydantic import BaseModel

class ItemBase(BaseModel):
    departamento: str
    item_nome: int
    matricula: int

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        orm_mode = True
