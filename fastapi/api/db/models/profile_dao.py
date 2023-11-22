from typing import List
from  datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Integer,
    Boolean,
    TIMESTAMP,
    ARRAY,
    String,
    func,
    cast
)
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship, Mapped, mapped_column

from api.db.db_config import Base


class ProfileDao(Base):
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    dark_theme: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    active_image: Mapped[str] = mapped_column(String, nullable=True)
    # images: Mapped[List[str]] = mapped_column(
    #     MutableList.as_mutable(postgresql.ARRAY(String)),
    #     nullable=True,
    #     server_default=cast(postgresql.array([]), ARRAY(String))
    # )
    images: Mapped[List[str]] = mapped_column(
        postgresql.ARRAY(String),
        nullable=True,
        default=cast(postgresql.array([]), ARRAY(String))
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete='CASCADE'),
        nullable=False
    )

    user: Mapped['UserDao'] = relationship('UserDao', back_populates='profile')
