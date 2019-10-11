from aiohttp import web
import aiohttp_cors
from .models import connect_db


async def hello(request):
    return web.Response(text="Hello, world")


async def create_app(config) -> web.Application:
    """
    返回aiohttp应用实例
    :return: web.Application
    """
    app = web.Application()
    app.add_routes([web.get('/', hello)])

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

    await connect_db(config.get('database'))

    return app
