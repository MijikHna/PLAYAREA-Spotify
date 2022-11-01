
"""create sheet tables

Revision ID: e620d4caea68
Revises: 550e3520b3fc
Create Date: 2022-08-07 19:43:10.607952

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = 'e620d4caea68'
down_revision = '550e3520b3fc'
branch_labels = None
depends_on = ['550e3520b3fc']


def create_sheet_tables_table() -> None:
    op.create_table(
        'sheet_tables',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Text, nullable=False),
        sa.Column(
            'created_at',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            'updated_at',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            'user_id',
            sa.Integer,
            sa.ForeignKey('users.id', ondelete='CASCADE'),
            nullable=False
        )
    )

    op.execute(
        """
        CREATE TRIGGER update_modtime
            BEFORE UPDATE
            ON sheet_tables
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_sheet_rows_table() -> None:
    op.create_table(
        'sheet_rows',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('number', sa.Text, nullable=False),
        sa.Column('height', sa.Integer, nullable=False, default=25),
        sa.Column(
            'updated_at',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            'table_id',
            sa.Integer, sa.ForeignKey('sheet_tables.id', ondelete='CASCADE'),
            nullable=True
        )
    )

    op.execute(
        """
        CREATE TRIGGER update_modtime
            BEFORE UPDATE
            ON sheet_rows
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_sheet_columns_table() -> None:
    op.create_table(
        'sheet_columns',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('notation', sa.Text, nullable=True),
        sa.Column('width', sa.Integer, nullable=False, default=100),
        sa.Column(
            'updated_at',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            'table_id',
            sa.Integer, sa.ForeignKey('sheet_tables.id', ondelete='CASCADE'),
            nullable=True
        )
    )

    op.execute(
        """
        CREATE TRIGGER update_modtime
            BEFORE UPDATE
            ON sheet_columns
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_sheet_cells_table() -> None:
    op.create_table(
        'sheet_cells',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('content', sa.Text, nullable=True),
        sa.Column(
            'updated_at',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            'table_id',
            sa.Integer, sa.ForeignKey('sheet_tables.id', ondelete='CASCADE'),
            nullable=True
        ),
        sa.Column(
            'row_id',
            sa.Integer, sa.ForeignKey('sheet_rows.id', ondelete='CASCADE'),
            nullable=True
        ),
        sa.Column(
            'column_id',
            sa.Integer, sa.ForeignKey('sheet_columns.id', ondelete='CASCADE'),
            nullable=True
        )
    )

    op.execute(
        """
        CREATE TRIGGER update_modtime
            BEFORE UPDATE
            ON sheet_cells
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def upgrade() -> None:
    create_sheet_tables_table()
    create_sheet_rows_table()
    create_sheet_columns_table()
    create_sheet_cells_table()


def downgrade() -> None:
    op.drop_table('sheet_tables')
    op.drop_table('sheet_rows')
    op.drop_table('sheet_columns')
    op.drop_table('sheet_cells')
