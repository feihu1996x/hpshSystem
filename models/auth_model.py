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
from utils.bytes_to_str_dict import bytes_to_str_dict


class AuthModel(BaseModel):
    """
    指标权限模型    
    """
    def get_auth_level(self, dims_name=None):
        if not dims_name:
            Logger.debug_logger().debug("参数dims_name为空")
            return {}

        redis_key = self.redis_key_prefix + "auth_table_" + str(dims_name)

        # 先尝试从redis中获取指标权限信息
        data = self.redis_db.hgetall(redis_key)

        if data:
            Logger.debug_logger().debug("从redis缓存中获取数据")
            print("从redis缓存中获取信息")
            # 将bytes字典转换成str字典
            data = bytes_to_str_dict(data)
        else:
            Logger.debug_logger().debug("从mysql中获取数据")
            sql = "SELECT ftable_name, flevel_id FROM auth_table WHERE ftable_name='{ftable_name}'".format(ftable_name=dims_name)
            data = self.mysql_db.execute_query_one_dict(sql)
            if data:
                self.redis_db.hmset(redis_key, data)  # 设置redis缓存
                self.redis_db.expire(redis_key, self.redis_key_expire_time)  # 设置缓存过期时间
        return data

