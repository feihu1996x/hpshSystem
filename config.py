#!/usr/bin/python3

"""
@file: config.py
@brief: 项目配置文件
@author: feihu1996.cn
@date: 18-08-17
@version: 1.0
"""

import os

# mysql连接配置
MYSQL_HOST="192.168.0.100"
MYSQL_PORT=3306
MYSQL_USER="test"
MYSQL_PASSWORD="*3!0CcEf"
MYSQL_DATABASE="hpshSystem"

# redis连接配置
REDIS_HOST="192.168.0.100"
REDIS_PORT=6379

# mongodb连接配置
MONGODB_HOST="192.168.0.100"
MONGODB_PORT=27017
MONGODB_DB="hpshSystem"

# hive连接配置
HIVE_HOST="192.168.0.101"
HIVE_PORT=10000
HIVE_USER="hadoop"

# 开发服务器配置
WEB_HOST="0.0.0.0"
WEB_PORT="8080"

# 日志配置
LOGGER_PATH=os.getcwd()+"/system.log"

# 发送邮件配置
MAIL_HOST="smtp.sina.com"
MAIL_FROM="qinxueonline@sina.com"
MAIL_TOLIST=["gsx0312@qq.com"]
MAIL_USERNAME="qinxueonline@sina.com"
MAIL_PASSWORD="admin123"

# session 配置
SESSION_COOKIE_NAME = 'session_id'
SECRET_KEY = 'a1GBZ9_x7)l7@8IuMt*'

