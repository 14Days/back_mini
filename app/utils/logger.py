# -*-coding:utf8-*-
__author__ = 'Abbott'

import logging

logger = logging.getLogger('main')


def create_base_log():
    logger.setLevel(level=logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)
