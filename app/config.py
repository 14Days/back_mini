# -*-coding:utf8-*-
__author__ = 'Abbott'


class FlaskConfig:
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:613fb94fbd740f66@wghtstudio.cn:3306/home_designer'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS = {
        'password': 'gyk199941',
        'host': 'wghtstudio.cn',
        'port': 6379
    }

    def __init__(self):
        pass
