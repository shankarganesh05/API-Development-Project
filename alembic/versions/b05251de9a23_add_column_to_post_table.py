"""Add column to post table

Revision ID: b05251de9a23
Revises: 437b56435f9f
Create Date: 2025-06-25 20:18:25.027689

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'b05251de9a23'
down_revision: Union[str, Sequence[str], None] = '437b56435f9f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('post',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('post','content')
    pass
