from app.database import Base 
from sqlalchemy import Column, Integer, String
from .database import Base 
from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    employee_name: str = Field("", description="O nome do funcionário")
    registration: str = Field("", description="A matrícula do funcionário")
    departament: str = Field("", description="O departamento do funcionário")
    item_name: str = Field("", description="O nome do item")
    description_item: str = Field("", description="A descrição do item")
    serial_number: str = Field("", description="O número de série do item")
    asset_serial_number: str = Field("", description="O número do patrimonio")
    item_status: str = Field("", description="A situação do item")

    class Config:
        orm_mode = True

class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True

class Items(Base):
    __tablename__ = "items" 
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_name = Column(String, nullable=False)
    registration = Column(String, nullable=False)
    departament = Column(String, nullable=False)
    item_name= Column(String, nullable=False)
    description_item= Column(String, nullable=False)
    serial_number= Column(String, nullable=False)
    asset_serial_number= Column(String, nullable=False)
    item_status= Column(String, nullable=False)

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    first_name: str = Field("", description="O nome do usuário")
    last_name: str = Field ("", description="Segundo nome")
    email: str = Field("", description="O email do usuário")
    password: str = Field("", description="A senha do usuário")
    registration: str = Field("", description="A matrícula do usuário")
    departament: str = Field("", description="O departamento do usuário")

class UserResponse(UserCreate):
    id: int = Field("", description="O ID do usuário")
    first_name: str = Field("", description="O nome do usuário")
    last_name: str = Field ("", description="Segundo nome")
    email: str = Field("", description="O email do usuário")
    password: str = Field("", description="A senha do usuário")
    resgistration: str = Field("", description="A matrícula do usuário")
    departament: str = Field("", description="O departamento do usuário")

    class Config:
        orm_mode = True

class Users(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False )
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    registration = Column(String, nullable=False)
    departament = Column(String, nullable=False)

    class Config:
        orm_mode = True