#!/usr/bin/python3

"""
@file: data_model.py
@brief: 数据模型
@author: feihu1996.cn
@date: 18-08-20
@version: 1.0
"""

import datetime

from models.base_model import BaseModel
from utils.logger import Logger
from utils.sql_tpl import SQL_TPL


class DataModel(BaseModel):
    """
    数据模型    
    """
    def get_data(self, dims='', args={}):
        """
        根据传进来的参数获取数据
        """
        sql = SQL_TPL.get(dims, None)
        if not sql:
            Logger.info_logger().info("无效的dims参数")
            return []
        
        sql = sql.format(start_date=args["start_date"], end_date=args["end_date"])

        """
        使用MongoDB缓存查询数据
        定时清除缓存
        {
            "sql": "使用的SQL语句",
            "flush_date": "刷新日期",
            "data": "查询数据"，
            "flush_count": "刷新频率"
        }
        """

        clause = {
            "sql": sql
        }
        datenow = datetime.datetime.now().date().strftime("%Y-%m-%d")

        # 从MongoDB中查找数据
        document = eval("self.mongo_db." + dims + ".find_one(clause)")
        if document: 
            Logger.info_logger().info("从MongoDB中查找数据") 
            # 更新刷新日期和刷新频率
            eval("self.mongo_db." + dims + ".update(clause, {'$set': {'flush_date': datenow}, '$inc': {'flush_count': 1}}, False, True)")
            results = document.get("data", [])
            print("从MongoDB中查找数据")
        else: # mongo缓存中没有数据
            Logger.info_logger().info("从mysql中查找数据")
            results = self.mysql_db.execute_query_list(sql)  # 表数据量很大时，查询会变得很慢
            for result in results:
                result[dims] = int(result[dims])
            document = {  # 构造文档
                "sql": sql,
                "data": results,
                "flush_date": datenow,
                "flush_count": 1
            }
            eval("self.mongo_db." + dims + ".insert_one(document)") # 向MongoDB中插入文档
            print("从mysql中查找数据")

        return results


if __name__ == "__main__":
    data = DataModel()
   
    # 插入测试数据 
    import datetime
    import random
    insert_sql = "insert into game_activity(fdate, fuser_id, fgame_id) values "
    sql_list = []
    for j in range(0, 10):
        fdate = (datetime.datetime.now().date() + datetime.timedelta(days=j)).strftime("%Y-%m-%d")
        temp = random.randrange(1, 1000)
        for i in range(0, temp):
            sql = "('{}', {}, {})".format(fdate, i+1000, i)
            sql_list.append(sql)
    insert_sql += ','.join(sql_list)

    print(data.mysql_db.execute_commit(insert_sql))

