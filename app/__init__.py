from aiohttp import web
import aiohttp_cors
from .controllers import register_routes
from .models import engine
from .utils.logger import create_base_log


async def create_app(config) -> web.Application:
    """
    返回aiohttp应用实例
    :return: web.Application
    """
    # 创建logger
    create_base_log(config['app'])

    # 获取顶级实例注册路由
    app = web.Application()
    register_routes(app)

    # 配置跨域访问
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            allow_headers="*",
            expose_headers="*"
        )
    })

    for route in list(app.router.routes()):
        cors.add(route)

    # 连接数据库
    await engine.connect_db(config.get('database'))

    # 注册关闭函数
    app.on_shutdown.append(engine.close_db)

    return app
