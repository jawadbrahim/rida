"""empty message

Revision ID: 8135a1126cf3
Revises: 
Create Date: 2023-12-04 09:38:40.135329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8135a1126cf3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('food',
    sa.Column('category', sa.String(length=250), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('picture', sa.String(length=500), nullable=True),
    sa.Column('ingredients', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('food')
    # ### end Alembic commands ###