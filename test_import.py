import sys
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models.models import Item


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

try:
    from app.database import SessionLocal, engine, Base
    print("Importação bem-sucedida!")
except Exception as e:
    print(f"Erro ao importar: {e}")