# app/models/models.py

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
