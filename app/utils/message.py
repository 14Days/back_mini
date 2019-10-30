# -*-coding:utf8-*-
__author__ = 'Abbott'

import random
import logging
import requests
from requests.exceptions import RequestException
from redis.exceptions import RedisError
from app.utils.redis import engine

logger = logging.getLogger('main.message')


def create_verify_code() -> str:
    code = ''
    for i in range(4):
        code += str(random.randint(0, 9))
    logger.info('Create verify code successfully')
    return code


def set_code_in_redis(phone: str, code: str):
    try:
        engine.engine.set(phone, code)
        engine.engine.expire(phone, 5 * 60)
        logger.info('Set code in redis successfully')
    except RedisError as e:
        logger.error('Failed to set data to redis', e)
        raise e


def get_code_in_redis(phone: str) -> str:
    try:
        return engine.engine.get(phone)
    except RedisError as e:
        logger.error('Failed to get data from redis', e)
        raise e


def send_message(phone: str, code: str) -> bool:
    try:
        r = requests.post('http://sms_developer.zhenzikj.com/sms/send.do', data={
            'appId': '102760',
            'appSecret': 'bb85649d-bd4a-4f48-9c0e-57e4d7c30855',
            'message': '欢迎注册家居设计小程序，您的注册验证码为:{0}（有效时间5分钟）'.format(code),
            'number': phone
        })
        response = r.json()
        if response['code'] != 0:
            raise RequestException()
    except RequestException as e:
        logger.error('Failed to send code', e)
        raise e
