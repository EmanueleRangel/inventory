from pydantic import BaseModel

class ItemBase(BaseModel):
    nome_funcionario: str
    matricula: str
    departamento: str
    nome_do_item: str
    quantidade_de_item: int
    descricao_do_item: str
    numero_de_serie_do_item: str
    numero_do_patrinomio: str
    situacao_do_item: str

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        orm_mode = True

class ItemUpdate(ItemBase):
    pass

class CriarUsuario(BaseModel):
    nome: str
    email: str
    password: str
    matricula: str
    departamento: str

    class Config:
        orm_mode = True
