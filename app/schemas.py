# schemas/item.py
from pydantic import BaseModel

class ItemCreate(BaseModel):
    nome: str
    matricula: str
    departamento: str
<<<<<<< HEAD
    item_nome: str  # Este campo deve corresponder ao campo 'item_nome' no modelo SQLAlchemy
=======
    item_nome: int
    matricula: int

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
>>>>>>> main

    class Config:
        orm_mode = True  # Permite conversão automática de objetos SQLAlchemy para Pydantic

class ItemResponse(ItemCreate):
    id: int  # Adiciona o campo 'id' para a resposta
