from aiohttp import web
from app.controllers.ping import Ping
from app.controllers.user import UserHandler


def register_routes(app: web.Application):
    ping_app = web.Application()
    ping = Ping()
    ping_app.router.add_get('', ping.hello)

    user_app = web.Application()
    user = UserHandler()
    user_app.router.add_get('/code', user.send_verify_code)
    user_app.router.add_get('/account', user.register_account)

    app.add_subapp('/ping', ping_app)
    app.add_subapp('/user', user_app)
