from fastapi import APIRouter, status, Depends

from api.logic.dto.user_dto import UserBaseDto, UserCreateDto, UserDto
from api.logic.services.user_service import UserService

user_router: APIRouter = APIRouter(
    prefix='/api/users',
    tags=['users']
)


@user_router.post(
    '/create',
    response_model=UserBaseDto,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    new_user: UserCreateDto,
    user_srv: UserService = Depends(UserService)
) -> UserBaseDto:
    created_user: UserBaseDto = user_srv.create_user(new_user)

    return created_user
