from fastapi import APIRouter, Depends

from services.utils import Response, ErrorResponse
from app.auth.auth_bearer import JWTBearer
from app.users import schemas, controller

users_routes = APIRouter()

@users_routes.patch('', dependencies=[Depends(JWTBearer())])
async def update_user(data: schemas.UpdateUserSchema):
    user = await controller.get_user(id=data.id)
    if not user:
        return ErrorResponse.not_found()
    _update_user = await controller.update_user(data)
    return Response(_update_user)

@users_routes.get('/{user_id}', dependencies=[Depends(JWTBearer())])
async def user_detail(user_id: int):
    user = await controller.get_user(id=user_id)
    if not user:
        return ErrorResponse.not_found()
    return Response(user)
