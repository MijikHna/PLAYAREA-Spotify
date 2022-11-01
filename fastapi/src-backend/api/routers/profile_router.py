from fastapi import APIRouter, status, Depends, UploadFile, HTTPException

from sqlalchemy.orm import Session

from api.logic.dto.user_dto import UserBaseDto
from api.logic.dto.profile_dto import ProfileDto
from api.logic.services.profile_service import ProfileService
from api.logic.utils.db_manager import open_db_session

from api.logic.utils.auth import get_user_from_token


profile_router: APIRouter = APIRouter(
    prefix='/api/profiles',
    tags=['profiles']
)


@profile_router.get(
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
    if username != user.username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )

    profile: ProfileDto = profile_srv.get_profile_by_username(
        db_session, username)

    return profile


@profile_router.put(
    '/',
    response_model=ProfileDto,
    status_code=status.HTTP_200_OK
)
async def update_profile(
    profile: ProfileDto,
    user: UserBaseDto = Depends(get_user_from_token),
    profile_srv: ProfileService = Depends(ProfileService),
    db_session: Session = Depends(open_db_session)
) -> ProfileDto:
    if profile.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Profile is not from logged in user'
        )

    return profile_srv.update_profile(db_session, profile)


@profile_router.post(
    '/picture',
    response_model=ProfileDto,
    status_code=status.HTTP_201_CREATED
)
async def add_picture(
    image: UploadFile,
    user: UserBaseDto = Depends(get_user_from_token),
    profile_srv: ProfileService = Depends(ProfileService),
    db_session: Session = Depends(open_db_session)
) -> ProfileDto:
    profile_dto: ProfileDto = await profile_srv.add_picture(
        image, user.id, db_session)

    return profile_dto
