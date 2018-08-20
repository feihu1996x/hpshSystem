#!/usr/bin/python3

"""
@file: clear_mongodb_cache.py
@brief: 清除MongoDB缓存 
@author: feihu1996.cn
@date: 18-08-20
@version: 1.0
"""

from pymongo import ASCENDING, DESCENDING


from models.base_model import BaseModel


class ClearMongoDBCache(BaseModel):
    """
    清除MongoDB缓存    
    """
    def __init__(self, collection_list=[]):
        self.max_count = 1000  # 最大缓存记录数
        self.collection_list = collection_list

    def clear_cache(self):
        for collection in collection_list:
            count = eval("self.mongo_db." + collection + ".count()")  # 当前缓存的总数
            overflow_count = count - self.max_count  # 当前缓存超出的总数 

            if overflow_count > 0:  # 当前缓存超出数量已经超过最大值
                # 对当前缓存按照flush_date和flush_count进行升序排序，然后取出超出max_count的那一部分数据
                res = eval("self.mongo_db." + collection + ".find().sort([('flush_date', ASCENDING), ('flush_count', ASCENDING)]).limit(overflow_count)")

                # 从筛选出的数据中取出sql字段作为后续的查询条件
                res_sql_list = [item.get('sql', '') for item in res]

                # 清除缓存
                eval("self.mongo_db." + collection + ".remove({'sql': {'$in': res_sql_list}})")
    

if __name__ == "__main__":
    # 待清除缓存的集合
    collection_list = ["game_activity"]

    db = ClearMongoDBCache(collection_list)
    """
    # 向缓存中插入测试数据
    from datetime import datetime, timedelta
    for collection in collection_list:
        for i in range(10):
            date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
            for j in range(100):
                document = {
                    "sql": "SELECT fdate, COUNT(fgame_id, {j}) AS game_activity FROM game_activity WHERE fdate>='{start_date}' AND fdate <='{end_date}' GROUP BY fdate;".format(start_date=date, end_date=date, j=j),
                    "flush_date": date,
                    "data": [j],
                    "flush_count": j
                }
                eval("db.mongo_db." + collection + ".insert_one(document)")
    """

    # 清除缓存
    db.clear_cache()

