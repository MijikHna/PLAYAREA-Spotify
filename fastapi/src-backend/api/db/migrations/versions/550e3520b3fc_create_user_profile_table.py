
"""create user profile table

Revision ID: 550e3520b3fc
Revises: 309b232de140
Create Date: 2022-04-17 21:04:20.615375

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '550e3520b3fc'
down_revision = '309b232de140'
branch_labels = None
depends_on = None


def create_profile_table() -> None:
    op.create_table(
        'profiles',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column(
            'theme',
            sa.Text,
            nullable=False,
            server_default='light'
        ),
        sa.Column('image', sa.Text, nullable=True),
        sa.Column(
            'user_id',
            sa.BigInteger,
            sa.ForeignKey('users.id', ondelete='CASCADE')
        ),
        sa.Column(
            'created_at',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
            index=False,
        ),
        sa.Column(
            'updated_at',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
            index=False,
        ),
    )

    op.execute(
        """
        CREATE TRIGGER update_user_modtime
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
