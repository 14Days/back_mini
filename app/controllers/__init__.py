from aiohttp import web
from .ping import ping


def register_routes(app: web.Application):
    ping_app = web.Application()
    ping_app.add_routes(ping)

    app.add_subapp('/ping', ping_app)
