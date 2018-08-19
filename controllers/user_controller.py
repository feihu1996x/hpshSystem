#!/usr/bin/python3

"""
@file: user_controller.py
@brief: 用户控制器
@author: feihu1996.cn
@date: 18-08-19
@version: 1.0
"""

from utils.response import Response
from controllers.base_controller import BaseController
from models.user_model import UserModel


class UserController(BaseController):
    """
    用户控制器   
    """
    def __init__(self, *args, **kwargs):
        super(UserController, self).__init__(*args, **kwargs)
        self.user = UserModel()

    def login(self):
        """
        用户登录
        """
        fwork_id = self.args.get("fwork_id", None) 
        fpassword = self.args.get("fpassword", None)

        if not fwork_id:
            return Response.responseJson(Response.INPUT_EMPTY, msg="账号为空")
        if not fpassword:
            return Response.responseJson(Response.INPUT_EMPTY, msg="密码为空")
       
        res = self.user.check_auth(fwork_id=fwork_id, fpassword=fpassword) 
        if res:
            self.session['fwork_id'] = fwork_id
            return Response.responseJson(Response.SUCCESS, msg='登录成功')
        else:
           return Response.responseJson(Response.ERROR, msg='账户或者密码错误') 

    def logout(self):
        """
        用户注销
        """
        self.session.pop("fwork_id", None)
        return Response.responseJson(Response.SUCCESS, msg='注销成功')

