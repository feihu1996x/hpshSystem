#!/usr/bin/python3

"""
@file: hive_base.py
@brief: Hive统计基类
@author: feihu1996.cn
@date: 18-08-22
@version: 1.0
"""

from pyhive import hive
import datetime

from utils.logger import Logger
import config


class HiveBase:
    """
    Hive统计基类    
    """
    def __init__(self):
        self.port = config.HIVE_PORT
        self.host = config.HIVE_HOST
        self.user = config.HIVE_USER
        self.today = datetime.datetime.now().date().strftime("%Y-%m-%d")

    def __call__(self):
        Logger.info_logger().info("正在创建hive表...")
        print("正在创建hive表...")
        if self.create_table():
            Logger.info_logger().info("hive表创建成功！")
            print("hive表创建成功！")
        else:
            Logger.info_logger().info("hive表创建失败！")
            print("hive表创建失败！")
            return None

        Logger.info_logger().info("开始统计...")
        print("开始统计...")
        if self.do_jobs():
            Logger.info_logger().info("统计完成...")
            print("统计完成...")
        else:
            Logger.info_logger().info("统计异常")
            print("统计异常")
            return None

    def create_table(self):
        """
        创建hive表
        """
        pass

    def do_jobs(self):
        """
        开始统计工作    
        """
        pass

    def execute(self, hql=None):
        try:
            print("正在执行hql:" + hql)
            Logger.debug_logger().debug("正在执行hql: {hql}".format(hql=hql))

            conn = hive.connect(host=self.host, port=self.port, username=self.user)
            
            cursor = conn.cursor()

            cursor.execute(hql)

            return True
        except Exception as e:
            Logger.error_logger().error("hive 执行异常")
            Logger.error_logger().error(e)

            return False
        finally:
            cursor.close()
            conn.close()
    
