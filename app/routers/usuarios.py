from typing import Optional

from fastapi import APIRouter, Body, Depends, status

from app.models.models import Usuarios, CriarUsuario, CriarUsuarioResponse


api_router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@api_router.post(
    "/create_user",
    status_code=status.HTTP_201_CREATED,
    description="Create user",
    # tags=tags,
    response_model=CriarUsuarioResponse,
    response_model_exclude_unset=True,
)
async def create_user(user: CriarUsuario = Body(...)):
    return user


# @api_router.get(
#     "/list_users",
#     status_code=status.HTTP_200_OK,
#     description="Get user list",
#     # tags=tags,
#     response_model=list[Usuarios],
#     response_model_exclude_unset=True,
# )
# async def get_user_list():
#     return