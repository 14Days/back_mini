import logging
from aiomysql.sa import create_engine


class DBEngine:
    engine = None

    async def connect_db(self, config):
        self.engine = await create_engine(minsize=config.get('pool'), user=config.get('user'),
                                          password=config.get('password'), host=config.get('host'),
                                          port=config.get('port'), db=config.get('db'))

    async def close_db(self, app):
        self.engine.close()
        await self.engine.wait_closed()


engine = DBEngine()
