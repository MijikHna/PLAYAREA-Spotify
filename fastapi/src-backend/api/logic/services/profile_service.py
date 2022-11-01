import os
from fastapi import Depends, UploadFile

from sqlalchemy.orm import Session
from api.db.db_config import DBSession

from api.db.models.profile_dao import ProfileDao
from api.db.models.user_dao import UserDao
from api.db.repositories.profile_repository import ProfileRepository
from api.logic.dto.profile_dto import ProfileDto
from api.logic.utils.db_manager import open_db_session


class ProfileService:
    def __init__(
        self,
        profile_repo: ProfileRepository = Depends(ProfileRepository)
    ) -> None:
        self.__profile_repo: ProfileRepository = profile_repo

    def get_profile_by_user(
        self,
        db_session: Session,
        user: UserDao,
    ) -> ProfileDto:
        try:
            profile_db: self.__profile_repo.get_profile_by_user(
                db_session,
                user
            )
        except Exception as e:
            raise e

        return ProfileDto(
            id=profile_db.id,
            theme=profile_db.theme,
            theme_options=profile_db.theme_options,
            image=profile_db.image,
            image_options=profile_db.image_options,
            user_id=profile_db.user_id
        )

    def get_profile_by_username(
        self,
        db_session: Session,
        username: str
    ) -> ProfileDto:
        try:
            profile_db: ProfileDao = self.__profile_repo.get_profile_by_username(
                db_session,
                username
            )
        except Exception as e:
            raise e

        return ProfileDto(
            id=profile_db.id,
            theme=profile_db.theme,
            theme_options=profile_db.theme_options,
            image=profile_db.image,
            image_options=profile_db.image_options,
            user_id=profile_db.user_id
        )

    def update_profile(
        self,
        db_session: Session,
        profile: ProfileDto,
    ) -> ProfileDto:

        try:
            profile_db: ProfileDao = self.__profile_repo.update_profile(
                db_session,
                profile
            )
            db_session.commit()
        except Exception as e:
            raise e

        return ProfileDto(
            id=profile_db.id,
            theme=profile_db.theme,
            theme_options=profile_db.theme_options,
            image=profile_db.image,
            image_options=profile_db.image_options,
            user_id=profile_db.user_id
        )

    async def add_picture(self, image: UploadFile, user_id: int, db_session: Session) -> ProfileDto:
        os.makedirs(f'static/{user_id}', exist_ok=True)

        with open(f'static/{user_id}/{image.filename}', 'wb') as file_stream:
            file_stream.write(await image.read())

        profile_db: ProfileDto = self.__profile_repo.add_picture(
            db_session, user_id, image.filename)

        db_session.commit()

        return ProfileDto(
            id=profile_db.id,
            theme=profile_db.theme,
            theme_options=profile_db.theme_options,
            image=profile_db.image,
            image_options=profile_db.image_options,
            user_id=profile_db.user_id
        )
