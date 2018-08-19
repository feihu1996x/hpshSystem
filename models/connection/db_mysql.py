#!/usr/bin/python3

"""
@file: db_mysql.py
@brief: 连接mysql数据库
@author: feihu1996.cn
@date: 18-08-19
@version: 1.0
"""

import pymysql
from pymysql.cursors import DictCursor

from utils.logger import Logger


class MySQLConnection:
    """
    MySQL数据库连接类
    """
    def __init__(self, host="127.0.0.1", port=3306, database=None, user=None, password=None, charset="utf8mb4"):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.charset = charset

    def execute_commit(self, sql=None):
        """
            执行SQL语句    
        """
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.database, charset=self.charset, cursorclass=DictCursor)
        try:
            Logger.info_logger().info("sql - {}".format(sql))
            
            with conn.cursor() as cursor:
                cursor.execute(sql)
                
            conn.commit()
            return True
        
        except Exception as e:
            Logger.error_logger().error("SQL执行异常--{}".format(e))
            conn.rollback()
            return False

        finally:
            conn.close()
            

    def execute_query(self, sql=None):
        """
        执行SQL（查询）
        """
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.database, charset=self.charset, cursorclass=DictCursor)
        try:
            data_list = []
            Logger.info_logger().info("sql - {}".format(sql))

            with conn.cursor() as cursor:
                cursor.execute(sql)
                data_list = cursor.fetchall()

            Logger.info_logger().info('sql data -- {}'.format(data_list))

        except Exception as e:
            Logger.error_logger().error('SQL执行异常--{}'.format(e))
            conn.rollback()

        finally:
            conn.close()
            return data_list

    def execute_query_one_dict(self, sql=None):
        """
        执行查询（返回第一条记录）
        """
        data = self.execute_query(sql)
        if data:
            return data[0]
        else:
            return {}

    def execute_query_list(self, sql=None):
        """
        执行查询（返回所有结果集组成的列表）    
        """
        return self.execute_query(sql)    


if __name__ == "__main__":
    db = MySQLConnection(host='192.168.0.100', port=3306, user='test', password='*3!0CcEf', database='hpshSystem')    
    # insert_sql = "INSERT INTO user_info SET fname = '章三', fwork_id=1001, fdept_id=1, flevel_id=1, fpassword='password'"
    # db.execute_commit(insert_sql)
    query_sql = "SELECT * FROM user_info"
    print(db.execute_query_list(query_sql))

