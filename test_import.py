<<<<<<< HEAD
# test_import.py
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
# test_import.py
>>>>>>> main

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

try:
    from app.database import SessionLocal, engine, Base
    print("Importação bem-sucedida!")
except Exception as e:
    print(f"Erro ao importar: {e}")
=======
<<<<<<< HEAD
from app.models.models import Item

print("Importação realizada com sucesso!")
>>>>>>> main
=======
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models.models import Item

# Criação de engine e sessão
engine = create_engine('sqlite:///:memory:')  # Use seu banco real aqui
Session = sessionmaker(bind=engine)
session = Session()

# Consulta correta (utilizando uma coluna do Item, não a classe)
result = session.query(Item).filter(Item.some_column == 'valor_especifico').all()

for item in result:
    print(item)
>>>>>>> 5b82b6b (add tests and improvements)
=======
# test_import.py
from app.models.models import Item

print("Importação realizada com sucesso!")
>>>>>>> 6286e90 (remove error from get list and post)
>>>>>>> main
