"""add content column to post table

Revision ID: c934a824cba3
Revises: 238df6168e35
Create Date: 2022-11-02 12:11:51.715861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c934a824cba3'
down_revision = '238df6168e35'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')

    pass