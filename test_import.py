# test_import.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

try:
    from app.database import SessionLocal, engine, Base
    print("Importação bem-sucedida!")
except Exception as e:
    print(f"Erro ao importar: {e}")
