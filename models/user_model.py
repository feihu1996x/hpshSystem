#!/usr/bin/python3

"""
@file: user_model.py
@brief: 用户模型
@author: feihu1996.cn
@date: 18-08-19
@version: 1.0
"""

from models.base_model import BaseModel
from utils.logger import Logger


class UserModel(BaseModel):
    """
    用户模型    
    """
    def check_auth(self, fwork_id=None, fpassword=None):
        """
        用户身份认证
        """
        if not fwork_id or not fpassword:
            Logger.debug_logger().debug("用户名或者密码为空")
            return False
        sql = "select * from user_info where fwork_id={fwork_id} and fpassword='{fpassword}'".format(fwork_id=fwork_id, fpassword=fpassword)
        Logger.debug_logger().debug("sql:" + sql)
        data = self.mysql_db.execute_query_one_dict(sql)
        return True if data else False

    def get_user_info(self, fwork_id):
        """
        获取用户信息
        """
        sql = "SELECT fname, fwork_id, fdept_id, flevel_id FROM user_info WHERE fwork_id={fwork_id}".format(fwork_id=fwork_id)
        data = self.mysql_db.execute_query_one_dict(sql)

        return data


