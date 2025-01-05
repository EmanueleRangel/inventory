# src/main.py
# main.py
from app.models.models import Item
from app.db import get_session

# Exemplo de uso
session = get_session()
result = session.query(Item).filter(Item.some_column == 'valor_especifico').all()

for item in result:
    print(item)

def main():
    print("Olá, mundo! Este é o meu novo projeto.")

if __name__ == "__main__":
    main()
