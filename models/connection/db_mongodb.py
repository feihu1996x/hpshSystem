#!/usr/bin/python3

"""
@file: db_mongodb.py
@brief: MongoDB数据库连接
@author: feihu1996.cn
@date: 18-08-19
@version: 1.0
"""

from pymongo import MongoClient


def mongodb_connection(host="127.0.0.1", port=27017, database=None):
    """
        MongoDB数据库连接
    """
    conn = MongoClient(host=host, port=port)
    db = eval("conn."+database)
    return db


if __name__ == "__main__":
    db = mongodb_connection(host="192.168.0.100", database="hpshSystem")
    print(db.test.insert_one({"a":1}))
    print(db.test.find_one())

