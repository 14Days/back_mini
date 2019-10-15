from aiohttp import web
import aiohttp_cors
from .utils.logger import create_base_log
from .middlewares.log import log_middleware
from .router import register_routes
from .models import engine
from .utils.redis import redis


async def create_app(config) -> web.Application:
    """
    返回aiohttp应用实例
    :return: web.Application
    """
    # 创建logger
    create_base_log(config['app'])

    # 获取顶级实例注册路由
    app = web.Application()
    app.middlewares.append(log_middleware)
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

    # 连接redis
    await redis.connect_redis(config.get('redis'))

    # 注册关闭函数
    app.on_cleanup.append(engine.close_db)
    app.on_cleanup.append(redis.close_redis)

    return app
