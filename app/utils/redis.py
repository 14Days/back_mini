# -*-coding:utf8-*-
__author__ = 'Abbott'

import logging
from flask import Flask
import redis

logger = logging.getLogger('main.redis')


class ConnectRedis:
    engine = None

    def connect_it(self, app: Flask):
        config = app.config['REDIS']
        try:
            self.engine = redis.Redis(host=config['host'], password=config['password'], port=config['port'])
            logger.info('Connect redis successfully')
        except redis.exceptions as e:
            logger.error('Failed to connect redis', exc_info=True)
            raise e


engine = ConnectRedis()
