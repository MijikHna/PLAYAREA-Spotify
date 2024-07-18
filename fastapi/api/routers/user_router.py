from sqlalchemy.orm import Session

from api.schemas.profile import BaseProfileDto, GetProfileDto, PutProfileDto
from api.schemas.user import CreateUserDto, LoggedInUserDto
from api.services.auth.auth_service import retrieve_user_from_token
from api.services.user_service import UserService
from api.utils.db_manager import open_db_session
from fastapi import APIRouter, Depends, HTTPException, UploadFile, status

user_router: APIRouter = APIRouter(
    prefix='/api/users',
    tags=['users']
)


@user_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(
    user_create: CreateUserDto,
    user_srv: UserService = Depends(UserService),
    db_session: Session = Depends(open_db_session)
) -> None:
    user_srv.create_user(db_session, user_create)


@user_router.get('/profile/{user_id}', response_model=GetProfileDto, status_code=status.HTTP_200_OK)
async def get_profile(
    user_id: int,
    user: LoggedInUserDto = Depends(retrieve_user_from_token),
    user_service: UserService = Depends(UserService),
    db_session=Depends(open_db_session)
) -> GetProfileDto:
    if (user_id != user.id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect logged in user'
        )

    profile: GetProfileDto = user_service.get_profile_by_user_id(db_session, user_id)

    return profile

@user_router.post(
    '/profile/image',
    response_model=BaseProfileDto,
    status_code=status.HTTP_201_CREATED
)
async def add_picture(
    image: UploadFile,
    user: LoggedInUserDto = Depends(retrieve_user_from_token),
    user_srv: UserService = Depends(UserService),
    db_session: Session = Depends(open_db_session)
) -> BaseProfileDto:
    profile: BaseProfileDto = user_srv.add_profile_picture(
        db_session, user.id, image)

    return profile

@user_router.put('/profile', response_model=BaseProfileDto, status_code=status.HTTP_200_OK)
async def update_profile(
    put_profile: PutProfileDto,
    user: LoggedInUserDto = Depends(retrieve_user_from_token),
    user_service: UserService = Depends(UserService),
    db_session: Session = Depends(open_db_session)
) -> BaseProfileDto:
    profile: BaseProfileDto = user_service.update_profile(
        db_session, user.id, put_profile)

    return profile
