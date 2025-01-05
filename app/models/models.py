from pydantic import BaseModel

class ItemCreate(BaseModel):
    nome: str
    matricula: str
    departamento: str
    item_nome: str

    class Config:
        orm_mode = True  # Permite que o Pydantic use o modelo SQLAlchemy
