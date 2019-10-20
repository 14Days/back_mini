import sqlalchemy as sa
import logging
from app.models import engine
from aiomysql.sa import Error

logger = logging.getLogger('main.user')
metadata = sa.MetaData()


class User:
    user = sa.Table(
        'user', metadata,
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('username', sa.VARCHAR(50), nullable=False),
        sa.Column('password', sa.VARCHAR(255), nullable=False),
        sa.Column('open_id', sa.VARCHAR(255), nullable=False),
        sa.Column('phone', sa.CHAR(11), nullable=False)
    )

    @classmethod
    async def check_phone(cls, phone: str) -> bool:
        try:
            async with engine.engine.acquire() as conn:
                res = await conn.execute(cls.user.select().where(cls.user.c.phone == phone))
                if await res.fetchone() is None:
                    return True
                else:
                    return False
        except Error as e:
            logger.error('Failed to select data from database')
            raise

    @classmethod
    async def check_user(cls, name):
        try:
            async with engine.engine.acquire() as conn:
                res = await conn.execute(cls.user.select().where(cls.user.c.username == name))
                if await res.fetchone() is None:
                    return True
                else:
                    return False
        except Error as e:
            logger.error('Failed to select data from database')
            raise

    @classmethod
    async def add_user(cls, name, password, phone):
        try:
            async with engine.engine.acquire() as conn:
                task = await conn.begin()
                await conn.execute(cls.user.insert().values(username=name, password=password, phone=phone, open_id='1'))
                await task.commit()
        except Error as e:
            logger.error('Failed to insert data to database')
            raise

    @classmethod
    async def check_password(cls, name, password):
        try:
            async with engine.engine.acquire() as conn:
                res = await conn.execute(
                    cls.user.select().where(cls.user.c.username == name).where(cls.user.c.password == password)
                )

                if await res.fetchone() is None:
                    return False
                else:
                    return True
        except Error as e:
            logger.error('Failed to confirm password from database')
            raise
