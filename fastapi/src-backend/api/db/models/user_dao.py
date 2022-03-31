from sqlalchemy import Column, ForeignKey, Integer, Boolean, Text, TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UserDao(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(Text, unique=True, nullable=True, index=True)
    email = Column(Text, unique=True, nullable=False, index=True)
    email_verified = Column(Boolean, nullable=False, server_default='False')
    password = Column(Text, nullable=False)
    is_active = Column(Boolean, nullable=False, server_default='False')
    is_superuser = Column(Boolean, nullable=False, server_default='False')
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        index=False,
        server_default='False'
    )
    updated_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        index=False,
        server_default='False'
    )
