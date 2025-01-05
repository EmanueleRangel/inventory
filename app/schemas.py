# app/schemas.py
from pydantic import BaseModel

class ItemBase(BaseModel):
    departamento: str
    itens: int

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        orm_mode = True
