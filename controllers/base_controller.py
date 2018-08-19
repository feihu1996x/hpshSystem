#!/usr/bin/python3

"""
@file: base_controller.py
@brief: 控制器基类
@author: feihu1996.cn
@date: 18-08-19
@version: 1.0
"""

from utils.logger import Logger


class BaseController:
    """
    控制器基类    
    """
    def __init__(self, args={}, session={}):
        """
        args：
            请求参数字典
        """
        Logger.info_logger().info("request args -- {}".format(args))

        self.args = args
        self.session = session
        
