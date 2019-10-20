import jwt
from .redis import redis
import time

key = 'secret'


def create_token(name: str) -> bytes:
    payload = {
        'name': name,
        'exp': time.time() + 10,
    }

    return jwt.encode(payload, key, 'HS256')


async def parse_token(token: bytes) -> dict:
    return jwt.decode(token, key, 'HS256')


async def set_name_in_redis(name: str, token: str):
    await redis.redis.set(name, token)
    # 设置过期时间为6小时
    await redis.redis.expire(name, 10)
