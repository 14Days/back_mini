import logging
import aioredis

logger = logging.getLogger('main.redis')


class Redis:
    redis = None

    async def connect_redis(self, config):
        try:
            self.redis = await aioredis.create_connection(
                'redis://:{}@{}:{}/0?encoding=utf-8'.format(config['password'], config['host'], config['port']))
            logger.info('Connect redis successfully')
        except aioredis.errors as e:
            logger.error('Failed to connect redis', exc_info=True)

    async def close_redis(self, app):
        self.redis.close()
        await self.redis.wait_closed()


redis = Redis()
