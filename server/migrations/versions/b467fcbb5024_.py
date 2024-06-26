"""empty message

Revision ID: b467fcbb5024
Revises: efa463c94a89
Create Date: 2024-04-02 12:31:31.531600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b467fcbb5024'
down_revision = 'efa463c94a89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('birds', sa.Column('image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('birds', 'image')
    # ### end Alembic commands ###
