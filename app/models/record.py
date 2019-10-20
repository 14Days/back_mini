import sqlalchemy as sa
import logging
import datetime
from .user import User
from app.models import engine
from sqlalchemy import ForeignKey

metadata = sa.MetaData()
logger = logging.getLogger('models.record')


class Record:
    record = sa.Table(
        'record', metadata,
        sa.Column('id', sa.INT, autoincrement=True, primary_key=True),
        sa.Column('user_id', sa.INT, ForeignKey('User.id')),
        sa.Column('day', sa.DATE, nullable=False),
        sa.Column('count', sa.INT, default=0, nullable=False)
    )

    # @classmethod
    # async def add_record_work(cls, name):
    #     try:
    #         user_id = User.get_user_id(name)
    #     except BaseException as e:
    #         logger.error('Failed to record work')
    #         raise
    #     finally:

    @classmethod
    async def get_work_today(cls, name: int) -> int:
        async with engine.engine.acquire() as conn:
            try:
                date = datetime.date.today()
                user_id = await User.get_user_id(name)
                res = await conn.execute(cls.record.select().where(cls.record.c.day == date).where(cls.record.c.user_id == user_id))
                temp = await res.fetchone()
                return temp[3]
            except BaseException as e:
                logger.error('Failed to get day from record')
                raise

