#!/usr/bin/python3

"""
@file: sqoop_base.py
@brief: Sqoop数据导出基类
@author: feihu1996.cn
@date: 18-08-24
@version: 1.0
"""

import datetime

import paramiko

from utils.logger import Logger
from models.connection.db_mysql import MySQLConnection
import config


class SqoopBase:
    """
    Sqoop数据导出基类
    """
    def __init__(self):
        self.host = config.HIVE_HOST
        self.port = config.HIVE_SSH_PORT
        self.user = config.HIVE_USER
        self.password = config.HIVE_SSH_PASSWORD

        self.today = datetime.datetime.now().date().strftime("%Y-%m-%d")

        self.mysql_host = config.MYSQL_HOST
        self.mysql_port = config.MYSQL_PORT
        self.mysql_database = config.MYSQL_DATABASE
        self.mysql_user = config.MYSQL_USER
        self.mysql_password = config.MYSQL_PASSWORD

        self.mysql_db = MySQLConnection(host=config.MYSQL_HOST, port=config.MYSQL_PORT, database=config.MYSQL_DATABASE, user=config.MYSQL_USER, password=config.MYSQL_PASSWORD)
        
        self._connect_ssh_host()
    
    def _connect_ssh_host(self):
        """
        ssh远程连接主机
        """
        try:
            Logger.info_logger().info("正在连接主机:{host} ...".format(host=self.host))
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            self.ssh.connect(hostname=self.host, 
                            port=self.port,
                            username=self.user,
                            password=self.password)
            Logger.info_logger().info("主机连接成功")
        except Exception as e:
            Logger.error_logger().error(e)

    def __call__(self):
        Logger.info_logger().info("正在创建数据表...")
        try: 
            self.create_table()
            Logger.info_logger().info("数据表创建成功！")
        except Exception as e:
            Logger.error_logger().error(e)
            return None

        Logger.info_logger().info("开始导出数据 ...")
        try:
            self.sqoop_jobs()
            Logger.info_logger().info("数据导出完成")
        except Exception as e:
            Logger.error_logger().error(e)
            return None

    def execute(self, cmd=None):
        """
        ssh远程执行命令
        """
        try:
            Logger.info_logger().info("cmd--{cmd}".format(cmd=cmd))
            stdin_info, stdout_info, stderr_info = self.ssh.exec_command(cmd)
        
            Logger.info_logger().info(stdout_info.read())
            Logger.info_logger().info(stderr_info.read())

            return stdout_info.read(), stderr_info.read()
        except Exception as e:
            Logger.error_logger().error(e)

    def create_table(self):
        """
        创建数据表，
        用于保存sqoop导出的数据,
        子类实现
        """
        pass

    def sqoop_jobs(self):
        """
        从hdfs中导出数据，
        子类实现
        """
        pass


if __name__ == "__main__":
    sqoop_base = SqoopBase()
    sqoop_base.execute("ls")

