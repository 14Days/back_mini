# -*-coding:utf8-*-
__author__ = 'Abbott'

import hashlib


def encode_md5(temp: str) -> str:
    md5 = hashlib.md5()

    md5.update(temp.encode(encoding='utf-8'))

    return md5.hexdigest()
