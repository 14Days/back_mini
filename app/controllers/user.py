# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from redis.exceptions import RedisError
from requests.exceptions import RequestException
from app.utils.warpper import success_warp, fail_warp
from app.models.user import check_phone
from app.utils.message import create_verify_code, set_code_in_redis, send_message

user_page = Blueprint('user', __name__, url_prefix='/user')


@user_page.route('/code', methods=['GET'])
def send_verify_code():
    phone = request.args.get('phone')

    if phone is None or phone == '':
        return fail_warp('缺少参数')

    try:
        if check_phone(phone) is not None:
            return fail_warp('电话号码已注册')
        code = create_verify_code()
        set_code_in_redis(phone, code)
        send_message(phone, code)
        return success_warp('发送成功')
    except SQLAlchemyError as e:
        return fail_warp('数据库操作失败')
    except RedisError as e:
        return fail_warp('redis操作失败')
    except RequestException as e:
        return fail_warp('验证码发送失败')
