from sqlalchemy import cast, ARRAY, String
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Session


from api.db.models.user_dao import UserDao
from api.db.models.profile_dao import ProfileDao
from api.logic.dto.profile_dto import ProfileDto


class ProfileRepository:
    def get_profile_by_user_id(self, db_session: Session, user_id: int) -> ProfileDao:
        profile_db: ProfileDao = db_session.query(
            ProfileDao).filter(ProfileDao.user_id == user_id).one()

        return profile_db

    def get_profile_by_username(self, db_session: Session, username: str) -> ProfileDao:
        profile_db: ProfileDao = db_session.query(ProfileDao).join(
            UserDao).filter(UserDao.username == username).one()

        return profile_db

    def create_profile(
        self,
        db_session: Session,
        profile: ProfileDto
    ) -> ProfileDao:
        profile_db: ProfileDao = ProfileDao(
            user_id=profile.user_id,
            theme=profile.theme,
        )

        db_session.add(profile_db)
        db_session.flush()

        return profile_db

    def update_profile(self, db_session: Session, profile: ProfileDto) -> ProfileDao:
        profile_db: ProfileDao = db_session.query(
            ProfileDao).filter(ProfileDao.id == profile.id).one()

        profile_db.theme = profile.theme
        profile_db.image = profile.image

        return profile_db

    def add_picture(self, db_session: Session, user_id, file_name: str) -> ProfileDao:
        profile_db: ProfileDao = db_session.query(
            ProfileDao).filter(ProfileDao.user_id == user_id).one()

        if file_name not in profile_db.image_options:
            profile_db.image_options.append(file_name)

        profile_db.image = file_name

        db_session.flush()

        return profile_db
