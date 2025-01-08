from app.database import Base 
from sqlalchemy import Column, Integer, String
from .database import Base  # Importe o Base do arquivo database.py
from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    nome_funcionario: str = Field("", description="O nome do funcionário")
    matricula: str = Field("", description="A matrícula do funcionário")
    departamento: str = Field("", description="O departamento do funcionário")
    nome_do_item: str = Field("", description="O nome do item")
    descricao_do_item: str = Field("", description="A descrição do item")
    numero_de_serie_do_item: str = Field("", description="O número de série do item")
    numero_de_serie_do_patrimonio: str = Field("", description="O número do patrimonio")
    situacao_do_item: str = Field("", description="A situação do item")

    class Config:
        orm_mode = True

class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True

class Item(Base):
    __tablename__ = "items"  # Nome da tabela no banco de dados
    id = Column(Integer, primary_key=True, autoincrement=True)  # Definindo 'id' como autoincremento
    nome_funcionario = Column(String, nullable=False)
    matricula = Column(String, nullable=False)
    departamento = Column(String, nullable=False)
    nome_do_item= Column(String, nullable=False)
    descricao_do_item= Column(String, nullable=False)
    numero_de_serie_do_item= Column(String, nullable=False)
    numero_de_serie_do_patrimonio= Column(String, nullable=False)
    situacao_do_item= Column(String, nullable=False)

    class Config:
        orm_mode = True

class CriarUsuario(BaseModel):
    nome: str = Field("", description="O nome do usuário")
    email: str = Field("", description="O email do usuário")
    password: str = Field("", description="A senha do usuário")
    matricula: str = Field("", description="A matrícula do usuário")
    departamento: str = Field("", description="O departamento do usuário")

class CriarUsuarioResponse(CriarUsuario):
    id: int = Field("", description="O ID do usuário")
    nome: str = Field("", description="O nome do usuário")
    email: str = Field("", description="O email do usuário")
    password: str = Field("", description="A senha do usuário")
    matricula: str = Field("", description="A matrícula do usuário")
    departamento: str = Field("", description="O departamento do usuário")

    class Config:
        orm_mode = True

class Usuarios(Base):
    __tablename__ = "usuarios"  # Nome da tabela no banco de dados
    id = Column(Integer, primary_key=True, autoincrement=True)  # Definindo 'id' como autoincremento
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    matricula = Column(String, nullable=False)
    departamento = Column(String, nullable=False)

    class Config:
        orm_mode = True