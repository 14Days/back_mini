# -*-coding:utf8-*-
__author__ = 'Abbott'

from flask import jsonify


class Base:
    @staticmethod
    def success_warp(data):
        return jsonify({
            'status': 'success',
            'data': data
        })

    @staticmethod
    def fail_warp(msg):
        return jsonify({
            'status': 'error',
            'err_msg': msg
        })
