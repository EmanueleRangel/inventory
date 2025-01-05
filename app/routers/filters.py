from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.models import Item
from app.models.database import get_db

router = APIRouter(prefix="/filters", tags=["Filters"])

@router.get("/")
def get_filters(db: Session = Depends(get_db)):
    departments = db.query(Item.departamento).distinct().all()
    items = db.query(Item.item_nome).distinct().all()
    return {
        "departments": [dep[0] for dep in departments],
        "items": [item[0] for item in items],
    }
