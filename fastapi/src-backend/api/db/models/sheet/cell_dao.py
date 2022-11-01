from sqlalchemy import Column, ForeignKey, Integer, BigInteger, Boolean, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship

from api.db.db_config import Base


class CellDao(Base):
    __tablename__ = 'sheet_cells'

    id: Column = Column(Integer, primary_key=True)
    content: Column = Column(Text, nullable=False)

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
    row_id: Column = Column(
        Integer,
        ForeignKey('sheet_rows.id', ondelete='CASCADE'),
        nullable=False
    )
    column_id: Column = Column(
        Integer,
        ForeignKey('sheet_columns.id', ondelete='CASCADE'),
        nullable=False
    )

    table = relationship('TableDao', back_populates='cells')
    row = relationship('RowDao', back_populates='cells')
    column = relationship('ColumnDao', back_populates='cells')
