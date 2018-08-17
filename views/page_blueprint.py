#!/usr/bin/python3

"""
@file: page_blueprint.py
@brief: 模板渲染蓝图 
@author: feihu1996.cn
@date: 18-08-17
@version: 1.0
"""

from flask import Blueprint, jsonify, g


page = Blueprint('page', __name__, url_prefix="/page")

@page.route("/index")
def index():
    print(g.request_args)
    return jsonify({"status": "ok"})

