"""Add remaining colms in Post Table

Revision ID: ba3f684c024c
Revises: 923c89f5b454
Create Date: 2025-06-25 20:40:07.964898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'ba3f684c024c'
down_revision: Union[str, Sequence[str], None] = '923c89f5b454'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('post', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('post', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('post','published')
    op.drop_column('post','created_at')
    pass
