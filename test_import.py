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
