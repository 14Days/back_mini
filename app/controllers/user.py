from aiohttp import web
from .base import Base
from app.utils.message import create_verify_code, set_code_in_redis, send_message, get_code_in_redis
from app.models.user import User
from app.utils.token import create_token, set_name_in_redis


class UserHandler(Base):
    # 注册接口
    async def send_verify_code(self, request: web.BaseRequest):
        try:
            phone_number = request.query.get('phone')

            if phone_number is None:
                return self.fail_warp('缺少参数')

            if phone_number == '':
                return self.fail_warp('参数不能为空字符串')

            if not await User.check_phone(phone_number):
                return self.fail_warp('已存在电话号码')

            code = create_verify_code()
            await set_code_in_redis(phone_number, code)
            result = await send_message(phone_number, code)
            if not result:
                return self.fail_warp('短信发送失败')
            return self.success_warp('短信发送成功')
        except BaseException as e:
            return self.fail_warp('数据库请求失败')

    async def register_account(self, request: web.BaseRequest):
        try:
            data = await request.json()
            name = data.get('name')
            password = data.get('password')
            phone = data.get('phone')
            code = data.get('code')

            if phone is None or code is None:
                return self.fail_warp('缺少参数')

            if phone == '' or code == '' or name == '' or password == '':
                return self.fail_warp('参数不能为空')

            if not await User.check_user(name):
                return self.fail_warp('用户名已存在')

            if code == await get_code_in_redis(phone):
                await User.add_user(name, password, phone)
                return self.success_warp('验证成功')
            else:
                return self.fail_warp('验证码错误')
        except BaseException as e:
            return self.fail_warp('数据库请求失败')

    # 登录接口
    async def login(self, request: web.BaseRequest):
        try:
            data = await request.json()
            name = data.get('name')
            password = data.get('password')

            if name is None or password is None:
                return self.fail_warp('缺少参数')

            if name == '' or password == '':
                return self.fail_warp('参数不能为空')

            if await User.check_user(name):
                return self.fail_warp('用户名不存在')

            if await User.check_password(name, password):
                token = create_token(name)
                try:
                    await set_name_in_redis(name, token)
                except BaseException as e:
                    return self.fail_warp('Redis存储失败')
                return self.success_warp(str(token, encoding='utf-8'))
            else:
                return self.fail_warp('登录失败')
        except BaseException as e:
            return self.fail_warp('数据库请求失败')
