<<<<<<< HEAD
# app/models/__init__.py
from .database import Base  # Certifique-se de que 'Base' está sendo importado corretamente
from .models import Item, ItemCreate, ItemResponse  # Outros modelos que você importará
=======
from app.models.models import Item, ItemCreate, ItemResponse  # Certifique-se de que os nomes estão corretos
from ..database import Base  # Importe Base a partir do banco de dados
>>>>>>> 6286e90 (remove error from get list and post)
