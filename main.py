from aiohttp import web
from app import create_app
from app.config import parse_config

config = parse_config()

app = create_app()

if __name__ == '__main__':
    web.run_app(app, port=config.get('app').get('port'))
