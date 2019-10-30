# -*-coding:utf8-*-
__author__ = 'Abbott'

import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger('main.models')

db = SQLAlchemy()


def connect_db(app: Flask):
    try:
        db.init_app(app)
        logger.info('Connect db successfully')
    except BaseException as e:
        logger.error('Failed to connect db', exc_info=True)


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e
