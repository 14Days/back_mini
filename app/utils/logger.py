import logging

logger = logging.getLogger('main')


def create_base_log(config):
    if config['mode'] == 'dev':
        logger.setLevel(level=logging.INFO)
    else:
        logger.setLevel(level=logging.ERROR)

    formatter = logging.Formatter(config['log']['format'])
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)
