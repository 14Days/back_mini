# -*-coding:utf8-*-
__author__ = 'Abbott'

import random
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from app.utils.redis import engine


def create_verify_code() -> str:
    code = ''
    for i in range(4):
        code += str(random.randint(0, 9))
    return code


def set_code_in_redis(phone: str, code: str):
    engine.engine.set(phone, code)
    engine.engine.expire(phone, 5 * 60)


def get_code_in_redis(phone: str) -> str:
    temp = engine.engine.get(phone)
    if temp is not None:
        return temp.decode('utf-8')
    else:
        raise RuntimeError('验证码过期')


def send_message(phone: str, code: str):
    client = AcsClient('LTAI4FqGKCfJu6zoTeokp7Zw', 'j4bhVYO0NseW2rVrVwzkvM6mElu2yr', 'cn-hangzhou')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "卷子生成系统")
    request.add_query_param('TemplateCode', "SMS_174276701")
    request.add_query_param('TemplateParam', json.dumps({
        'code': code
    }))

    response = client.do_action_with_exception(request)
    temp = json.loads(str(response, encoding='utf-8'))

    if temp['Message'] != 'OK':
        raise RuntimeError(temp['Message'])
