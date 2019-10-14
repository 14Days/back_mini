import sqlalchemy as sa
from . import engine

metadata = sa.MetaData()


class Notice:
    notice = sa.Table(
        'notice', metadata,
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.VARCHAR(255), nullable=False),
        sa.Column('summary', sa.VARCHAR(1024), nullable=False),
        sa.Column('content', sa.VARCHAR(1024), nullable=True),
        sa.Column('push_day', sa.DateTime, nullable=False)
    )

    async def select_all(self):
        async with engine.engine.acquire() as conn:
            res = await conn.execute(self.notice.select())
            return await res.fetchall()
