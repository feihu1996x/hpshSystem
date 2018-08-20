#!/usr/bin/python3

"""
@file: base_model.py
@brief: 数据库连接模型基类
@author: feihu1996.cn
@date: 18-08-19
@version: 1.0
"""

from models.connection import db_mongodb, db_redis, db_mysql
import config


class BaseModel:
    """
        数据库连接模型基类
    """
    redis_db = db_redis.redis_connection(host=config.REDIS_HOST, 
                                         port=config.REDIS_PORT)
    mongo_db = db_mongodb.mongodb_connection(host=config.MONGODB_HOST, 
                                             port=config.MONGODB_PORT,
                                             database=config.MONGODB_DB)
    mysql_db = db_mysql.MySQLConnection(host=config.MYSQL_HOST,
                                        port=config.MYSQL_PORT,
                                        user=config.MYSQL_USER,
                                        password=config.MYSQL_PASSWORD,
                                        database=config.MYSQL_DATABASE)
    
    def __init__(self):
        # redis key过期时间
        self.redis_key_expire_time = 60*60*24
        
        # redis key 前缀
        self.redis_key_prefix = "hpshSystem_"
        
