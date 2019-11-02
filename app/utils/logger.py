# -*-coding:utf8-*-
__author__ = 'Abbott'

import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask


def create_base_log(app: Flask):
    handler = TimedRotatingFileHandler(
        "flask.log", when="D", interval=1, backupCount=15,
        encoding="UTF-8", delay=False, utc=False)

    formatter = logging.Formatter('[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s')
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)

    app.logger.setLevel(level=logging.INFO)
