import random
import json
import aiohttp
import logging
from app.utils.redis import redis

logger = logging.getLogger('main.message')


def create_verify_code() -> str:
    code = ''
    for i in range(4):
        code += str(random.randint(0, 9))
    logger.info('Create verify code successfully')
    return code


async def set_code_in_redis(phone_number: str, code: str):
    try:
        await redis.redis.set(phone_number, code)
        await redis.redis.expire(phone_number, 5 * 60)
        logger.info('Set code in redis successfully')
    except IOError as e:
        logger.error('Failed to set data to redis')


async def get_code_in_redis(phone_number: str) -> str:
    try:
        return await redis.redis.get(phone_number)
    except IOError as e:
        logger.error('Failed to get data from redis')


async def send_message(phone_number: str, code: str) -> bool:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post('http://sms_developer.zhenzikj.com/sms/send.do', data={
                'appId': '102760',
                'appSecret': 'bb85649d-bd4a-4f48-9c0e-57e4d7c30855',
                'message': '欢迎注册家居设计小程序，您的注册验证码为:{0}'.format(code),
                'number': phone_number
            }) as response:
                result = await response.text()
                logger.info('Get response successfully')
        except ConnectionError as e:
            logger.error('Failed to get response from zhen zi')
        try:
            result = json.loads(result)
            if result['code'] == 0:
                return True
            else:
                return False
        except ValueError as e:
            logger.error('Failed to parse json data')
