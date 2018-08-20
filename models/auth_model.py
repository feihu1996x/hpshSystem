#!/usr/bin/python3

"""
@file: auth_model.py
@brief: 指标权限模型
@author: feihu1996.cn
@date: 18-08-20
@version: 1.0
"""

from models.base_model import BaseModel
from utils.logger import Logger


class AuthModel(BaseModel):
    """
    指标权限模型    
    """
    def get_auth_level(self, dims_name=None):
        if not dims_name:
            Logger.debug_logger().debug("参数dims_name为空")
            return {}

        sql = "SELECT ftable_name, flevel_id FROM auth_table WHERE ftable_name='{ftable_name}'".format(ftable_name=dims_name)
        data = self.mysql_db.execute_query_one_dict(sql)
        return data

