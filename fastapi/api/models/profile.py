from datetime import datetime
from typing import List

from sqlalchemy import (
    ARRAY,
    TIMESTAMP,
    Boolean,
    ForeignKey,
    Integer,
    String,
    cast,
    func,
)
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.config.db_config import Base


class ProfileModel(Base):
    __tablename__ = "profiles"

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
        default=cast(postgresql.array([]), ARRAY(String)),
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    user: Mapped["UserModel"] = relationship("UserModel", back_populates="profile")
