from sqlalchemy import Column, Integer, ForeignKey, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship

from api.db.db_config import Base


class TableDao(Base):
    __tablename__ = 'sheet_tables'

    id: Column = Column(Integer, primary_key=True)
    name: Column = Column(Text, nullable=False)

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
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )

    user = relationship('UserDao', back_populates='tables')

    rows = relationship('RowDao', back_populates='table')
    columns = relationship('ColumnDao', back_populates='table')
    cells = relationship('CellDao', back_populates='table')
