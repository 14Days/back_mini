# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Flask
from app.middlewares.token import jwt_middleware
from app.controllers.user import user_page
from app.controllers.notice import notice_page
from app.controllers.img import img_page


def register_routers(app: Flask):
    app.register_blueprint(user_page)
    jwt_middleware(notice_page)
    app.register_blueprint(notice_page)
    jwt_middleware(img_page)
    app.register_blueprint(img_page)
