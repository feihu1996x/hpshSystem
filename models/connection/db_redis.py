#!/usr/bin/python3

"""
@file: db_redis.py
@brief: Redis数据库连接
@author: feihu1996.cn
@date: 18-08-19
@version: 1.0
"""

import redis


def redis_connection(host="127.0.0.1", port=6379):
    """
        Redis数据库连接
    """
    pool = redis.ConnectionPool(host=host, port=port)
    redis_cli = redis.Redis(connection_pool=pool)
    return redis_cli


if __name__ == "__main__":
    db = redis_connection(host="192.168.0.100")
    db.set("test", "test")
    print(db.get("test"))

