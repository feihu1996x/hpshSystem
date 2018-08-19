#!/usr/bin/python3

"""
@file: page_blueprint.py
@brief: 模板渲染蓝图 
@author: feihu1996.cn
@date: 18-08-17
@version: 1.0
"""

from flask import Blueprint, jsonify, render_template, g, session


from controllers.user_controller import UserController
from utils.auth import Auth

user = Blueprint('user', __name__, url_prefix="/user")


@user.route("/login", methods=["POST"])
def login():
    return jsonify(UserController(args=g.request_args, session=session).login())

@user.route("/logout", methods=["POST"])
def logout():
    return jsonify(UserController(args=g.request_args, session=session).logout());

@user.route("/testAuth", methods=["GET"])
@Auth.login_require
def testAuth():
    from utils.response import Response
    return jsonify(Response.responseJson(Response.SUCCESS))

