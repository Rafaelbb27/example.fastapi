"""add user table

Revision ID: 69a89e0e9954
Revises: c934a824cba3
Create Date: 2022-11-02 12:47:53.136157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69a89e0e9954'
down_revision = 'c934a824cba3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
    )

    pass


def downgrade():
    op.drop_table('users')
    pass
