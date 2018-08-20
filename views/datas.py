#!/usr/bin/python3

"""
@file: datas.py
@brief: 数据蓝图 
@author: feihu1996.cn
@date: 18-08-20
@version: 1.0
"""

from flask import Blueprint, jsonify, g, session


from utils.auth import Auth
from utils.response import Response
from controllers.data_controller import DataController


data = Blueprint('data', __name__, url_prefix="/data")

@data.route("/get_data", methods=["GET"])
@Auth.login_require
def get_data():
    return jsonify(DataController(args=g.request_args, session=session).get_data())

