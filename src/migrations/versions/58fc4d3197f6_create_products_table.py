"""Create products table

Revision ID: 58fc4d3197f6
Revises: 
Create Date: 2021-05-21 20:02:18.067173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58fc4d3197f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###