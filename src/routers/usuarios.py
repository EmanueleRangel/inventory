from typing import List, Optional
from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.models import Users, UserCreate, UserResponse
from src.models.database import SessionLocal

api_router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@api_router.post(
    "/create_user",
    status_code=status.HTTP_201_CREATED,
    description="Create user",
    response_model=UserResponse,
    response_model_exclude_unset=True,
)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = Users(**user.dict()) 
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error while creating item: " + str(e))

@api_router.get(
    "/users_list",
    status_code=status.HTTP_200_OK,
    description="Get user list",
    response_model=List[UserResponse],
    response_model_exclude_unset=True,
)
async def get_user_list(db: Session = Depends(get_db)):
    try:
        users = db.query(Users).all()  
        if not users:
            raise HTTPException(status_code=404, detail="No users found")
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))