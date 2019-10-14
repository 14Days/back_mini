import logging
from aiohttp import web

logger = logging.getLogger('main.middleware')


@web.middleware
async def log_middleware(request, handler):
    if request.method == 'GET':
        logger.info({
            'url': request.url,
            'method': request.method
        })
    else:
        logger.info({
            'url': request.url,
            'method': request.method,
            'body': await request.json()
        })

    response = await handler(request)
    logger.info({
        'status': response.status,
        'body': response.body
    })
    return response
