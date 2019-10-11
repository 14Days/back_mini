from aiohttp import web
from app.controllers import hello


def register_routes(app: web.Application):
    app.add_routes([web.get('/ping', hello)])
