#!/usr/bin/python3

"""
@file: page_blueprint.py
@brief: 模板渲染蓝图 
@author: feihu1996.cn
@date: 18-08-17
@version: 1.0
"""

from flask import Blueprint, jsonify, render_template

from utils.response import Response

user = Blueprint('user', __name__, url_prefix="/user")

@user.route("/login", methods=["POST"])
def login():
    return jsonify(Response.responseJson(Response.SUCCESS, data=[]));

@user.route("/logout", methods=["POST"])
def logout():
    return jsonify(Response.responseJson(Response.SUCCESS, data=[]));

