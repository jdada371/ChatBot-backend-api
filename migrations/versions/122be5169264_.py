"""empty message

Revision ID: 122be5169264
Revises: 3a818309fd44
Create Date: 2021-11-15 19:27:04.846988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '122be5169264'
down_revision = '3a818309fd44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat_log', sa.Column('date', sa.String(length=200), nullable=False))
    op.add_column('chat_log', sa.Column('student_time', sa.String(length=200), nullable=True))
    op.add_column('chat_log', sa.Column('bot_response_time', sa.String(length=200), nullable=True))
    op.add_column('chat_log', sa.Column('student_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'chat_log', 'student', ['student_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'chat_log', type_='foreignkey')
    op.drop_column('chat_log', 'student_id')
    op.drop_column('chat_log', 'bot_response_time')
    op.drop_column('chat_log', 'student_time')
    op.drop_column('chat_log', 'date')
    # ### end Alembic commands ###
