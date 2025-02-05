from app.models.database import engine
from app.models import Items

Items.metadata.create_all(bind=engine)
