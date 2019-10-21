from aiohttp import web
from app import create_app
from app.config import parse_config


async def init_app():
    config = parse_config()
    app = await create_app(config)
    return app


if __name__ == '__main__':
    web.run_app(init_app())
