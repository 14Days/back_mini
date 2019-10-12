from aiomysql.sa import create_engine

engine = None


async def connect_db(config):
    global engine
    engine = await create_engine(minsize=config.get('pool'), user=config.get('user'),
                                 password=config.get('password'), host=config.get('host'),
                                 port=config.get('port'), db=config.get('db'))


async def close_db(app):
    global engine
    engine.close()
    await engine.wait_closed()
