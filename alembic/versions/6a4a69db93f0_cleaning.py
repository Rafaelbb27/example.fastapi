"""cleaning

Revision ID: 6a4a69db93f0
Revises: 69e05aa8d4b8
Create Date: 2022-11-02 14:59:55.482183

"""
from alembic import op
import sqlalchemy as sa

# add last few columns to post table
# revision identifiers, used by Alembic.
revision = '6a4a69db93f0'
down_revision = '69e05aa8d4b8'
branch_labels = None
depends_on = None
# add last few columns to post table
# add last few columns to post table
def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
        ('NOW()')),)

    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
