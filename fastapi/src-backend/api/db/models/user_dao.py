from sqlalchemy import Column, Integer, Boolean, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship

from api.db.db_config import Base


class UserDao(Base):
    __tablename__ = 'users'

    id: Column = Column(Integer, primary_key=True)
    username: Column = Column(Text, unique=True, nullable=True)
    email: Column = Column(Text, unique=True, nullable=False)
    email_verified: Column = Column(
        Boolean,
        nullable=False,
        server_default='False'
    )
    password: Column = Column(Text, nullable=False)
    is_active: Column = Column(
        Boolean,
        nullable=False,
        server_default='False'
    )
    is_superuser: Column = Column(
        Boolean,
        nullable=False,
        server_default='False'
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

    profile = relationship('ProfileDao', back_populates='user', uselist=False)
    tables = relationship('TableDao', back_populates='user')
