from aiohttp import web
from app.controllers.ping import Ping


def register_routes(app: web.Application):
    ping_app = web.Application()
    ping = Ping()
    ping_app.router.add_get('', ping.hello)

    app.add_subapp('/ping', ping_app)
