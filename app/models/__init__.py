import logging
from aiomysql.sa import create_engine, Error

logger = logging.getLogger('main.models')


class DBEngine:
    engine = None

    async def connect_db(self, config):
        try:
            self.engine = await create_engine(user=config.get('user'),
                                              password=config.get('password'), host=config.get('host'),
                                              port=config.get('port'), db=config.get('db'))
            logger.info('Connect db successfully')
        except Error as e:
            logger.error('Failed to connect db', exc_info=True)

    async def close_db(self, app):
        self.engine.close()
        await self.engine.wait_closed()


engine = DBEngine()
