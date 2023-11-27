from typing import List
from sqlalchemy import Integer, Boolean, String, TIMESTAMP, func
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from api.db.db_config import Base


class UserDao(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email_verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default='False'
    )
    password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default='False'
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default='False'
    )
    created_at: Mapped[int] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    updated_at: Mapped[int] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    refresh_token: Mapped[str] = mapped_column(String,  nullable=True)

    profile: Mapped['ProfileDao'] = relationship('ProfileDao', back_populates='user', uselist=False)
    # tables: Mapped[List['TableDao']|None] = relationship(back_populates='user')

    __table_args__ = (UniqueConstraint("username", name='uq_username_users'),)
    __table_args__ = (UniqueConstraint("email", name='uq_email_users'),)
