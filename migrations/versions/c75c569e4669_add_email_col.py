"""add email col

Revision ID: c75c569e4669
Revises: c85747b0289e
Create Date: 2020-05-05 12:47:43.093486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c75c569e4669'
down_revision = 'c85747b0289e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###