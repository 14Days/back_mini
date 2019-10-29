# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Flask
from flask_cors import CORS
from app.utils.logger import create_base_log
from app.config import FlaskConfig
from app.models import connect_db


def new_flask_app():
    # 创建基础logger
    create_base_log()

    app = Flask(__name__)
    CORS(app)

    # 添加配置文件
    app.config.from_object(FlaskConfig)

    # 链接数据库
    connect_db(app=app)

    return app
