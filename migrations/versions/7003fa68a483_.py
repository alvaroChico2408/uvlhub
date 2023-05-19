"""empty message

Revision ID: 7003fa68a483
Revises: d8daab31e725
Create Date: 2023-05-19 10:13:12.837955

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7003fa68a483'
down_revision = 'd8daab31e725'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fm_metrics', schema=None) as batch_op:
        batch_op.alter_column('solver',
               existing_type=mysql.VARCHAR(length=120),
               type_=sa.Text(),
               existing_nullable=True)
        batch_op.alter_column('not_solver',
               existing_type=mysql.VARCHAR(length=120),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fm_metrics', schema=None) as batch_op:
        batch_op.alter_column('not_solver',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(length=120),
               existing_nullable=True)
        batch_op.alter_column('solver',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(length=120),
               existing_nullable=True)

    # ### end Alembic commands ###