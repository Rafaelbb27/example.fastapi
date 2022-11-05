"""add user table2

Revision ID: 69e05aa8d4b8
Revises: 69a89e0e9954
Create Date: 2022-11-02 13:37:06.470412

"""
from alembic import op
import sqlalchemy as sa

#add foreing key
# revision identifiers, used by Alembic.
revision = '69e05aa8d4b8'
down_revision = '69a89e0e9954'
branch_labels = None
depends_on = None
#add foreing key
def upgrade():  
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
    local_cols=[
                        'owner_id'], remote_cols=['id'], ondelete="CASCADE")

    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts','owner_id')

    pass