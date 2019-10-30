# -*-coding:utf8-*-
__author__ = 'Abbott'

import time
import jwt
from app.utils.redis import engine

key = 'secret'


def create_token(username: str) -> bytes:
    payload = {
        'name': username,
        'exp': time.time() + 6 * 24 * 60 * 60,
    }

    return jwt.encode(payload, key, 'HS256')


def parse_token(token: bytes) -> dict:
    return jwt.decode(token, key, 'HS256')


def set_name_in_redis(name: str, token: bytes):
    engine.engine.set(name, token)
    # 设置过期时间为6天
    engine.engine.expire(name, 6 * 24 * 60 * 60)
