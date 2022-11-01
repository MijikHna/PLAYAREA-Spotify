from turtle import width
from sqlalchemy import Column, ForeignKey, Integer, BigInteger, Boolean, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship

from api.db.db_config import Base


class ColumnDao(Base):
    __tablename__ = 'sheet_columns'

    id: Column = Column(Integer, primary_key=True)
    notation: Column = Column(Text, nullable=False)
    width: Column = Column(Integer, nullable=False, default=100)

    updated_at: Column = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    table_id: Column = Column(
        Integer,
        ForeignKey('sheet_tables.id', ondelete='CASCADE'),
        nullable=False
    )

    table = relationship('TableDao', back_populates='columns')
    cells = relationship('CellDao', back_populates='column')
