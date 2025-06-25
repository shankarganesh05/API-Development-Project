"""add votes table

Revision ID: 06673ede4751
Revises: ba3f684c024c
Create Date: 2025-06-25 20:43:40.433833

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '06673ede4751'
down_revision: Union[str, Sequence[str], None] = 'ba3f684c024c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('vote',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )

    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('vote')
    pass
