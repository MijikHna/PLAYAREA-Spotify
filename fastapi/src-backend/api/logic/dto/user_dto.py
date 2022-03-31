from typing import Optional
from api.logic.dto.id_mixin import IdMixin


class UserDto(IdMixin):
    username: Optional[str]
    email: Optional[str]
    password: str


class UserBaseDto(IdMixin):
    username: str
    email: str


class UserCreateDto(UserBaseDto):
    email_verified: bool = False
    password: str
    password_confirm: str
    is_superuser: bool = False


class UserEditDto(UserBaseDto):
    email_verified: str
    password: str
    is_active: bool
    is_superuser: bool
