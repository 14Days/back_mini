from aiohttp import web


async def hello(request):
    return web.Response(text="Hello, world")


def create_app() -> web.Application:
    app = web.Application()
    app.add_routes([web.get('/', hello)])

    return app
