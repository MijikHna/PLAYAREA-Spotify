from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.orm import Session

from api.logic.dto.profile_dto import ProfileDto
from api.logic.dto.user_dto import UserBaseDto, UserCreateDto, UserDto
from api.logic.services.user_service import UserService
from api.logic.services.profile_service import ProfileService
from api.logic.utils.auth import get_user_from_token
from api.logic.utils.db_manager import open_db_session

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
    user: UserCreateDto,
    user_srv: UserService = Depends(UserService),
    db_session: Session = Depends(open_db_session)
) -> UserBaseDto:
    print(user)
    created_user: UserBaseDto = user_srv.create_user(db_session, user)

    return created_user


@user_router.get(
    '/{username}',
    response_model=ProfileDto,
    status_code=status.HTTP_200_OK
)
async def get_profile(
    username: str,
    user: UserBaseDto = Depends(get_user_from_token),
    profile_srv: ProfileService = Depends(ProfileService),
    db_session=Depends(open_db_session)
) -> ProfileDto:
    if (username != user.username):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect logged in user'
        )

    profile: ProfileDto = profile_srv.get_profile_by_username(
        db_session, username)

    return profile
