"""add userid in post

Revision ID: ddcda77f8732
Revises: 06673ede4751
Create Date: 2025-06-25 21:10:44.514134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'ddcda77f8732'
down_revision: Union[str, Sequence[str], None] = 'ba3f684c024c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('post',sa.Column('user_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk', source_table="post", referent_table="users", local_cols=[
                          'user_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('post','user_id')
    pass
