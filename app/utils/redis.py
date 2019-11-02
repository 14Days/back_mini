# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Flask
import redis


class ConnectRedis:
    engine = None

    def connect_it(self, app: Flask):
        config = app.config['REDIS']
        try:
            self.engine = redis.Redis(host=config['host'], password=config['password'], port=config['port'])
            app.logger.info('Connect redis successfully')
        except redis.exceptions as e:
            app.logger.error('Failed to connect redis', exc_info=True)
            raise e


engine = ConnectRedis()
