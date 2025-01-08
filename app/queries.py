from app.database import get_session
from app.models.models import Item

session = get_session()

session.query(Item).filter(Item.some_column == 'valor').all()