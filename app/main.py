from fastapi import FastAPI
from plotly.io import to_html
from sqlalchemy.orm import Session
from app.models.database import SessionLocal, engine, Base
from app.routers import items, upload, usuarios
from app.models.database import engine
import app.models as models
from app.models import Items
from app.models.database import engine, Base
from app.models.models import Items, Users
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_sample_data(db: Session):
    item1 = Items(departamento="TI", itens=10)
    item2 = Items(departamento="RH", itens=20)
    db.add(item1)
    db.add(item2)
    db.commit()

@app.on_event("startup")
def on_startup():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router)
app.include_router(upload.router)
app.include_router(usuarios.api_router)

sys.dont_write_bytecode = True

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

Base.metadata.create_all(bind=engine)