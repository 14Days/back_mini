import sqlalchemy as sa
from app.models import engine
import logging

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
        except ConnectionError as e:
            logger.error('Failed to select data from database')

    @classmethod
    async def add_user(cls, name, password, phone):
        try:
            async with engine.engine.acquire() as conn:
                print(cls.user.insert().values(username=name, password=password, phone=phone, open_id='1'))
                print(name)
                print(password)
                print(phone)
                await conn.execute(cls.user.insert().values(username=name, password=password, phone=phone, open_id='1'))
        except IOError as e:
            logger.error('Failed to insert data to database')


