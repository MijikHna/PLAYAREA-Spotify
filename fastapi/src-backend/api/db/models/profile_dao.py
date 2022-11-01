from sqlalchemy import Column, ForeignKey, Integer, Text, TIMESTAMP, ARRAY, String, func, cast
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship

from api.db.db_config import Base


class ProfileDao(Base):
    __tablename__ = 'profiles'

    id: Column = Column(Integer, primary_key=True)
    theme: Column = Column(Text, nullable=False)
    theme_options: Column = Column(
        MutableList.as_mutable(postgresql.ARRAY(String)),
        nullable=False,
        server_default=postgresql.array(['light', 'dark'])
    )
    image: Column = Column(Text, nullable=True)
    image_options: Column = Column(
        MutableList.as_mutable(postgresql.ARRAY(String)),
        nullable=False,
        server_default=cast(postgresql.array([]), ARRAY(String))
    )
    created_at: Column = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    updated_at: Column = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    user_id: Column = Column(
        Integer,
        ForeignKey("users.id", ondelete='CASCADE'),
        nullable=False
    )

    user = relationship('UserDao', back_populates='profile')
