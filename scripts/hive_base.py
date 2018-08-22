#!/usr/bin/python3

"""
@file: hive_base.py
@brief: Hive统计基类
@author: feihu1996.cn
@date: 18-08-22
@version: 1.0
"""

from pyhive import hive

from utils.logger import Logger


class HiveBase:
    """
    Hive统计基类    
    """
    def __init(self, port=None, host=None):
        self.port = port 
        self.host = host

    def __call__(self):
        Logger.info_logger().info("正在创建统计结果表...")
        print("正在创建统计结果表...")
        if self.create_table():
            Logger.info_logger().info("统计结果表创建成功！")
            print("统计结果表创建成功！")
        else:
            Logger.info_logger().info("统计结果表创建失败！")
            print("统计结果表创建失败！")

        Logger.info_logger().info("开始统计...")
        print("开始统计...")
        if self.do_jobs():
            Logger.info_logger().info("统计完成...")
            print("统计完成...")
        else:
            Logger.info_logger().info("统计异常")
            print("统计异常")

    def create_table(self):
        """
        创建hive统计结果表
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

            conn = hive.connnect(host=self.host, port=self.port)
            
            cursor = conn.cursor()

            cursor.execute(hql)

            cursor.commit()

            return True
        except Exception as e:
            Logger.error_logger().error("hive 执行异常")

            return False
        finally:
            cursor.close()
            conn.close()
    
