from src.database import get_session
from src.models.models import Items

session = get_session()

session.query(Items).filter(Items.some_column == 'valor').all()