"""Add the column Created_at in products table

Revision ID: 49e791333a18
Revises: 58fc4d3197f6
Create Date: 2021-05-21 20:17:57.076229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49e791333a18'
down_revision = '58fc4d3197f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('created_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'created_at')
    # ### end Alembic commands ###
