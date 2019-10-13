from aiohttp import web
import aiohttp_cors
from .controllers import register_routes
from .models import engine


async def create_app(config) -> web.Application:
    """
    返回aiohttp应用实例
    :return: web.Application
    """
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

    await engine.connect_db(config.get('database'))

    app.on_shutdown.append(engine.close_db)

    return app
