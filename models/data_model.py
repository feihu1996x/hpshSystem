#!/usr/bin/python3

"""
@file: data_model.py
@brief: 数据模型
@author: feihu1996.cn
@date: 18-08-20
@version: 1.0
"""

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
        results = self.mysql_db.execute_query_list(sql)
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

