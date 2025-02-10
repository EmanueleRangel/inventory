from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.models.models import Items, ItemResponse, ItemCreate
from fastapi.responses import JSONResponse, HTMLResponse
from src.models.database import SessionLocal
from src.utils import generate_graph
from src.models import Items

router = APIRouter()

router = APIRouter(prefix="/itens", tags=["Itens"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ItemResponse])  
async def get_items(db: Session = Depends(get_db)):
    try:
        items = db.query(Items).all()  
        if not items:
            raise HTTPException(status_code=404, detail="No items found")
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    try:
        db_item = Items(**item.dict()) 
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error while creating item: " + str(e))



@router.get("/grafico", response_class=JSONResponse)
async def get_graph(db: Session = Depends(get_db)):
    items = db.query(Items).all()
    graph_json = generate_graph(items)
    return JSONResponse(content=graph_json)

def main():
    statement = select(Items.items)

if __name__ == "__main__":
    main()
    try:
        items = db.query(Items).all()  # type: ignore # A consulta agora está correta para retornar todos os itens
        if not items:
            raise HTTPException(status_code=404, detail="No items found for graph generation")  # Verifica se há itens
        graph_json = generate_graph(items)  # Gera o gráfico
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error generating graph: " + str(e))

@router.get("/grafico", response_class=HTMLResponse)
def get_graph_html(db: Session = Depends(get_db)):
    try:
        items = db.query(Items).all()
        return generate_graph(items)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error generating graph: " + str(e))

def get_graph(db: Session = Depends(get_db)):
    items = db.query(Items).all()  
    return generate_graph(items) 

@router.get("/grafico", response_class=JSONResponse)
async def get_graph(db: Session = Depends(get_db)):
        items = db.query(Items).all()  
        if not items:
            raise HTTPException(status_code=404, detail="No items found for graph generation")
        graph_json = generate_graph(items)
        return JSONResponse(content=graph_json)  
