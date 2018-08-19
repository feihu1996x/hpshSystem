#!/usr/bin/python3

"""
@file: logger.py
@brief: 系统日志:
    1. 窗口日志
    2. 文件日志
    3. 邮件报警日志
@author: feihu1996.cn
@date: 18-08-19
@version: 1.0
"""

import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler, SMTPHandler

import config

"""
logging输出格式化选项：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名|
%(funcName)s 调用日志输出函数的函数名|
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮点数表示|
%(relativeCreated)d 输出日志信息时的，自Logger创建以来的毫秒数|
%(asctime)s 字符串形式的当前时间。默认格式是“2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s 用户输出的消息
"""


class Logger:
    """
    系统日志    
    """
    logger_name = "system"

    @classmethod
    def debug_logger(cls):
        logging.basicConfig(level=logging.DEBUG)
        cls().add_stream_handler()
        return logging.getLogger(cls.logger_name)
    
    @classmethod
    def info_logger(cls):
        logging.basicConfig(level=logging.INFO)
        cls().add_file_handler()
        return logging.getLogger(cls.logger_name)
    
    @classmethod
    def error_logger(cls):
        logging.basicConfig(level=logging.ERROR)
        cls().add_email_handler()
        return logging.getLogger(cls.logger_name)

    def add_stream_handler(self):
        '''
        窗口日志
        :return:
        '''
        stream_handler = StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s [%(pathname)s:%(lineno)d]'))
        logging.getLogger(self.logger_name).addHandler(stream_handler)    

    def add_file_handler(self):
        '''
        文件日志
        :return:
        '''
        file_handler = RotatingFileHandler(config.LOGGER_PATH, maxBytes=1024*1024*500, delay=False, backupCount=20)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s [%(pathname)s:%(lineno)d]'))
        logging.getLogger(self.logger_name).addHandler(file_handler)

    def add_email_handler(self):
        '''
        email报警日志
        :return:
        '''
        email_handler = SMTPHandler(mailhost=config.MAIL_HOST, fromaddr=config.MAIL_FROM, toaddrs=config.MAIL_TOLIST, subject='hpshSystem error', credentials=(config.MAIL_USERNAME, config.MAIL_PASSWORD), secure=())
        email_handler.setLevel(logging.ERROR)
        email_handler.setFormatter(logging.Formatter('''
                Message type : %(levelname)s
                Location : %(pathname)s:%(lineno)d
                Module : %(module)s 
                Function : %(funcName)s 
                Time : %(asctime)s
                Message :
                  %(message)s '''))
        logging.getLogger(self.logger_name).addHandler(email_handler)

if __name__ == "__main__":
    # 输出窗口日志
    # Logger.debug_logger().debug("debug")

    # 输出文件日志
    # Logger.info_logger().info("xxoo")

    # 输出email报警日志
    Logger.error_logger().error("xxoo")
    
