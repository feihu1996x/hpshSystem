#!/usr/bin/python3

"""
@file: auth.py
@brief: 登录认证类
@author: feihu1996.cn
@date: 17-11-19
@version: 1.0
"""

from flask import session, jsonify
from utils.response import Response


class Auth():
    """
    登录认证
    """
    @classmethod
    def login_require(self, func):
        def wrap(*args, **kwargs):
            if not session.get('fwork_id', None):
                return jsonify(Response.responseJson(Response.NO_LOGIN))
            return func(*args, **kwargs)
        return wrap

