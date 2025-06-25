"""Create Post Table

Revision ID: 437b56435f9f
Revises: 
Create Date: 2025-06-25 20:06:49.803814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '437b56435f9f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    #op.create_table(table_name="post",sa.Column("id",sa.Integer(),nullable=False,primary_key=True,"title",sa.String(),nullable=False)
    op.create_table('post', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("post")
    pass
