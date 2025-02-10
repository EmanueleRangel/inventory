from src.models.database import engine
from src.models import Items

Items.metadata.create_all(bind=engine)
