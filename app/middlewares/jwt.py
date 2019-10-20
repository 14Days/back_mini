from aiohttp import web


@web.middleware
async def jwt_middleware(request: web.BaseRequest, handler):
    headers = request.headers


