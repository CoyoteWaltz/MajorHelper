"""empty message

Revision ID: 4c3dc03da84f
Revises: 
Create Date: 2019-05-07 16:30:22.175661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c3dc03da84f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_class_chief_id'), 'class', ['chief_id'], unique=False)
    op.add_column('student', sa.Column('nick_name', sa.String(length=20), nullable=True))
    op.create_index(op.f('ix_student_class_id'), 'student', ['class_id'], unique=False)
    op.create_unique_constraint(None, 'student', ['nick_name'])
    op.create_index(op.f('ix_teacher_class_id'), 'teacher', ['class_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_teacher_class_id'), table_name='teacher')
    op.drop_constraint(None, 'student', type_='unique')
    op.drop_index(op.f('ix_student_class_id'), table_name='student')
    op.drop_column('student', 'nick_name')
    op.drop_index(op.f('ix_class_chief_id'), table_name='class')
    # ### end Alembic commands ###