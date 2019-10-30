# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Blueprint, request, g
from redis import RedisError
from jwt.exceptions import ExpiredSignatureError, DecodeError
from app.utils.redis import engine
from app.utils.warpper import fail_warp
from app.utils.token import parse_token


def jwt_middleware(app: Blueprint):
    @app.before_request
    def decode_token():
        token = request.headers.get('token')
        if token is None:
            return fail_warp('请携带token'), 401

        try:
            jwt = parse_token(bytes(token, encoding='utf-8'))
            username = jwt['name']
            if engine.engine.get(username) is None:
                return fail_warp('jwt不存在，请重新登录'), 401
            g.username = username
        except ExpiredSignatureError:
            return fail_warp('jwt已过期，请重新登录'), 401
        except DecodeError:
            return fail_warp('jwt错误'), 401
        except RedisError:
            return fail_warp('redis错误'), 401
