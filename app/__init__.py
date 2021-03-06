# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Flask
from flask_cors import CORS
from app.utils.logger import create_base_log
from app.config import FlaskConfig
from app.controllers import register_routers
from app.models import connect_db
from app.utils.redis import engine


def new_flask_app():
    app = Flask(__name__)
    CORS(app)

    # 创建基础logger
    create_base_log(app)

    # 添加配置文件
    app.config.from_object(FlaskConfig)

    # 注册路由
    register_routers(app)

    # 链接数据库
    connect_db(app=app)

    # 链接redis
    engine.connect_it(app)

    return app
