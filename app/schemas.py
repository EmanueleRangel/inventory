from pydantic import BaseModel

class ItemCreate(BaseModel):
    nome: str
    matricula: str
    departamento: str
    item_nome: str

    class Config:
        orm_mode = True  # Permite a conversão de objetos SQLAlchemy para dict

class ItemResponse(ItemCreate):
    id: int
