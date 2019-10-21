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

    @classmethod
    async def get_work_today(cls, name: str) -> dict:
        async with engine.engine.acquire() as conn:
            try:
                date = datetime.date.today()
                user_id = await User.get_user_id(name)
                res = await conn.execute(
                    cls.record.select().where(cls.record.c.day == date).where(cls.record.c.user_id == user_id))
                temp = await res.fetchone()
                res1 = await conn.execute(
                    'select sum(count) from record where day between (select date_sub(curdate(), INTERVAL WEEKDAY(curdate()) + 1 DAY)) and (select date_sub(curdate(), INTERVAL WEEKDAY(curdate()) - 5 DAY))')
                temp1 = await res1.fetchone()

                return {
                    'day': temp[3],
                    'week': str(temp1[0])
                }
            except BaseException:
                logger.error('Failed to get data from record')
                raise

    @classmethod
    async def add_day_record(cls, name: str):
        async with engine.engine.acquire() as conn:
            try:
                date = datetime.date.today()
                user_id = await User.get_user_id(name)

                res = await conn.execute(
                    cls.record.select().where(cls.record.c.day == date).where(cls.record.c.user_id == user_id))
                temp = await res.fetchone()

                if temp is None:
                    await conn.execute(cls.record.insert().values(user_id=user_id, day=date, count=1))
                else:
                    count = temp[3] + 1
                    task = await conn.begin()
                    await conn.execute(cls.record.update().where(cls.record.c.user_id == user_id).where(
                        cls.record.c.day == date).values(count=count))
                    await task.commit()
            except BaseException:
                logger.error('Failed to refresh record to database')
                raise
