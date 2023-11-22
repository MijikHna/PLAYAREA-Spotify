
"""create user table

Revision ID: 309b232de140
Revises:
Create Date: 2022-01-25 21:57:49.209847

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '309b232de140'
down_revision = None
branch_labels = None
depends_on = None

# helper functions


def create_updated_at_trigger() -> None:
    op.execute(
        """
        CREATE OR REPLACE FUNCTION update_updated_at_column()
            RETURNS TRIGGER AS
        $$
        BEGIN
            NEW.updated_at = now();
            RETURN NEW;
        END;
        $$ language 'plpgsql';
        """
    )


def create_users_table() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column(
            'username',
            sa.Text,
            unique=True,
            nullable=True,
        ),
        sa.Column('email', sa.Text, unique=True, nullable=False),
        sa.Column(
            'email_verified',
            sa.Boolean,
            nullable=False,
            server_default='False'
        ),
        sa.Column('password', sa.Text, nullable=False),
        sa.Column(
            'is_active',
            sa.Boolean(),
            nullable=False,
            server_default='True'
        ),
        sa.Column(
            'is_superuser',
            sa.Boolean(),
            nullable=False,
            server_default='False'
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
    )

    op.create_unique_constraint("uq_username_users", "users", ["username"])
    op.create_unique_constraint("uq_email_users", "users", ["email"])


    op.execute(
        """
        CREATE TRIGGER update_modtime
            BEFORE UPDATE
            ON users
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def upgrade() -> None:
    create_updated_at_trigger()
    create_users_table()


def downgrade() -> None:
    op.drop_table("users")
    op.execute("DROP FUNCTION update_updated_at_column")
