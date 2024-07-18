import logging
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import or_, select, update
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from api.config.config_fastapi import PlayareaConfig, get_playarea_config
from api.exceptions.incorrect_password_exception import \
    IncorrectPasswordException
from api.exceptions.user_not_found_exception import UserNotFoundException
from api.models.user import UserModel
from api.schemas.token import TokenDataSchema, TokenSchema
from api.schemas.user import LoggedInUserDto, LoginUserDto
from api.utils.db_manager import open_db_session
from fastapi import Cookie, Depends

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/auth/token_fastapi')

playarea_config: PlayareaConfig = get_playarea_config()


class AuthService:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.info('AuthService init')

        self.__password_context = CryptContext(
            schemes=['bcrypt'],
            deprecated='auto'
        )

    def _verify_password(self, plain_password, hashed_password):
        return self.__password_context.verify(plain_password, hashed_password)

    def _hash_password(self, password):
        return self.__password_context.hash(password)

    def _authenticate_user(
        self,
        db_session: Session,
        user_login: LoginUserDto,
    ) -> UserModel:
        try:
            user: Optional[UserModel] = db_session.scalars(select(UserModel).where(or_(UserModel.email == user_login.login_identifier, UserModel.username == user_login.login_identifier))).first()

            if user is None:
                raise UserNotFoundException

        except NoResultFound:
            raise UserNotFoundException

        if not self._verify_password(user_login.password, user.password):
            raise IncorrectPasswordException

        return user

    def create_user_token(self, db_session: Session, user_login: LoginUserDto) -> TokenSchema:
        try:
            user: UserModel = self._authenticate_user(db_session, user_login)
        except Exception as e:
            raise e

        token_data: TokenDataSchema = TokenDataSchema(
            id = user.id,
            user_identifier=user.email if user.email else user.username
        )
            
        # TODO: move to a function
        to_encode_token: Dict[str, Any] = token_data.model_dump()
        to_encode_refresh_token: Dict[str, Any] = token_data.model_dump()

        token_expires_at: datetime = datetime.now() +\
            timedelta(minutes=playarea_config.access_token_expire_minutes)

        refresh_token_expires_at: datetime = datetime.now() + timedelta(hours=playarea_config.refresh_token_expire_minutes)

        to_encode_token.update({'exp': token_expires_at })
        to_encode_refresh_token.update({'exp': refresh_token_expires_at})
        
        encoded_token_jwt: str = jwt.encode(
            to_encode_token,
            playarea_config.secret_key,
            algorithm=playarea_config.algorithm
        )
        
        encoded_refresh_jwt: str = jwt.encode(
            to_encode_refresh_token,
            playarea_config.secret_key,
            algorithm=playarea_config.algorithm
        )

        user.refresh_token = encoded_refresh_jwt;
        db_session.commit()

        return TokenSchema(access_token=encoded_token_jwt, refresh_token=encoded_refresh_jwt, token_type='bearer')

    def renew_token(self, refresh_token: str, db_session: Session):
        user: Optional[UserModel] = db_session.execute(select(UserModel).where(UserModel.refresh_token == refresh_token)).scalars().first()

        if not user:
            raise Exception('User not found')

        token_data: TokenDataSchema = TokenDataSchema(
            id = user.id,
            user_identifier=user.email if user.email else user.username
        )

        to_encode_token: Dict[str, Any] = token_data.model_dump()

        token_expires_at: datetime = datetime.now() +\
            timedelta(minutes=playarea_config.access_token_expire_minutes)

        to_encode_token.update({'exp': token_expires_at })
        
        encoded_token_jwt: str = jwt.encode(
            to_encode_token,
            playarea_config.secret_key,
            algorithm=playarea_config.algorithm
        )
        

        return TokenSchema(access_token=encoded_token_jwt, refresh_token=refresh_token, token_type='bearer')

    def retrieve_user_from_token(
        self,
        db_session: Session,
        token: str,
    ) -> LoggedInUserDto:
        try:
            decoded_token = jwt.decode(
                token,
                playarea_config.secret_key,
                algorithms=[playarea_config.algorithm]
            )

            print(decoded_token)

            user: Optional[UserModel] = db_session.scalars(select(UserModel).where(UserModel.id == decoded_token.get('id'))).one()

            if user is None:
                raise UserNotFoundException

        except NoResultFound:
            raise UserNotFoundException
        except JWTError:
            raise UserNotFoundException
        except Exception as e:
            raise e

        return LoggedInUserDto(
            id=user.id,
            username=user.username,
            email=user.email
        )

    def logout_user(self, user_id: int, db_session: Session) -> None:
        print(user_id)
        try:
            db_session.execute(update(UserModel).where(UserModel.id == user_id).values(refresh_token=None))
        except Exception as e:
            raise e

def retrieve_user_from_token(
    # token: str = Depends(oauth2_scheme),
    token: str = Cookie(alias='Authorization'),
    auth_srv: AuthService = Depends(AuthService),
    db_session: Session = Depends(open_db_session)
) -> LoggedInUserDto:
    print(token)
    try:
        user: LoggedInUserDto = auth_srv.retrieve_user_from_token(db_session, token)
    except Exception as e:
        raise e
    print('retrieve', user)
    return user

