
"""create user profile table

Revision ID: 550e3520b3fc
Revises: 309b232de140
Create Date: 2022-04-17 21:04:20.615375

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.mutable import MutableList


# revision identifiers, used by Alembic
revision = '550e3520b3fc'
down_revision = '309b232de140'
branch_labels = None
depends_on = ['309b232de140']


def create_profile_table() -> None:
    op.create_table(
        'profiles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column(
            'theme',
            sa.Text,
            nullable=False,
            server_default='light'
        ),
        sa.Column(
            'theme_options',
            MutableList.as_mutable(postgresql.ARRAY(sa.String)),
            nullable=False,
            server_default=postgresql.array(['light', 'dark'])
        ),
        sa.Column('image', sa.Text, nullable=True),
        sa.Column(
            'image_options',
            MutableList.as_mutable(postgresql.ARRAY(sa.String)),
            nullable=False,
            server_default=sa.cast(postgresql.array([]), sa.ARRAY(sa.String))
        ),
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
            sa.ForeignKey("users.id", ondelete='CASCADE'),
            nullable=False
        ),
    )

    op.execute(
        """
        CREATE TRIGGER update_modtime
            BEFORE UPDATE
            ON profiles
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def upgrade() -> None:
    create_profile_table()


def downgrade() -> None:
    op.drop_table('profiles')
