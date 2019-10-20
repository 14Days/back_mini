import logging
from jwt.exceptions import ExpiredSignatureError, DecodeError
from aiohttp import web
from app.utils.redis import redis
from app.utils.token import parse_token
from app.controllers.base import Base

logger = logging.getLogger('main.jwt')


@web.middleware
async def jwt_middleware(request: web.BaseRequest, handler):
    headers = request.headers
    token = bytes(headers['token'], encoding='utf-8')

    try:
        jwt = await parse_token(token)
    except ExpiredSignatureError:
        logger.error('JWT has expired')
        return Base.fail_warp('jwt已过期,请重新登录')
    except DecodeError:
        logger.error('Failed to decode JWT')
        return Base.fail_warp('jwt错误')

    if redis.redis.get(jwt['name']) is None:
        return Base.fail_warp('jwt不存在,请重新登录')

    response = await handler(request)
    return response
