from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from app.models.models import Item, ItemResponse, ItemCreate  # Certifique-se de que os modelos estão corretos
from app.models.database import SessionLocal  # Sessão do banco de dados
from app.visualizations import generate_graph_from_items  # Função para gerar o gráfico

# Configuração do roteador
router = APIRouter(prefix="/itens", tags=["Itens"])

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota GET: Recupera todos os itens
@router.get("/", response_model=List[ItemResponse])  # Retorna uma lista de itens
async def get_items(db: Session = Depends(get_db)):
    try:
        items = db.query(Item).all()
        if not items:
            raise HTTPException(status_code=404, detail="No items found")  # Retorna 404 se não encontrar itens
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Trata possíveis erros

# Rota POST: Cria um novo item
@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    try:
        db_item = Item(**item.dict())  # Cria o objeto Item com os dados recebidos
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        db.rollback()  # Reverte transação em caso de erro
        raise HTTPException(status_code=500, detail="Error while creating item: " + str(e))

# Rota GET: Gera o gráfico e retorna como JSON
@router.get("/grafico", response_class=JSONResponse)
async def get_graph_data(db: Session = Depends(get_db)):
    try:
        items = db.query(Item).all()
        if not items:
            raise HTTPException(status_code=404, detail="No items found")
        
        # Gera os dados da tabela no formato JSON
        graph_data = generate_graph_from_items(items)
        return JSONResponse(content=graph_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching items: {str(e)}")
