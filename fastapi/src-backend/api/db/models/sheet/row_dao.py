from sqlalchemy import Column, ForeignKey, Integer, BigInteger, Boolean, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship

from api.db.db_config import Base


class RowDao(Base):
    __tablename__ = 'sheet_rows'

    id: Column = Column(Integer, primary_key=True)
    number: Column = Column(Text, nullable=False)
    height: Column = Column(Integer, nullable=False, default=25)

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

    table = relationship('TableDao', back_populates='rows')
    cells = relationship('CellDao', back_populates='row')
