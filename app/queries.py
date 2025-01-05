from app.database import get_session
from app.models.models import Item
#from app.db import get_session  # Supondo que você tenha uma função para obter a sessão

session = get_session()

session.query(Item).filter(Item.some_column == 'valor').all()