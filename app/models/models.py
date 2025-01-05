# app/models.py

from app.database import Base  # Importação absoluta
from sqlalchemy import Column, Integer, String

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    matricula = Column(String)
    departamento = Column(String, index=True)
    item_nome = Column(String)

    def __repr__(self):
        return f"<Item(nome={self.nome}, matricula={self.matricula}, departamento={self.departamento}, item_nome={self.item_nome})>"
