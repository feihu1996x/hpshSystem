#!/usr/bin/python3

"""
@file: page_blueprint.py
@brief: 模板渲染蓝图 
@author: feihu1996.cn
@date: 18-08-17
@version: 1.0
"""

from flask import Blueprint, jsonify, render_template

user = Blueprint('user', __name__, url_prefix="/user")

@user.route("/login", methods=["POST"])
def login():
    data = {
        "code": 0,
        "msg": "登录成功",
        "data": []
    }
    return jsonify(data);

@user.route("/logout", methods=["POST"])
def logout():
    data = {
        "code": 0,
        "msg": "注销成功",
        "data": []
    }
    return jsonify(data);

