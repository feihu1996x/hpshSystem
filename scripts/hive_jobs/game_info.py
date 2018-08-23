#!/usr/bin/python3

"""
@file: game_info.py
@brief: 使用hive创建游戏信息表并导入数据
@author: feihu1996.cn
@date: 18-08-22
@version: 1.0
"""

from scripts.hive_base import HiveBase


class GameInfo(HiveBase):
    """
    使用hive创建用户信息表并导入数据
    """
    def create_table(self):
        """
        hive建表语句,
        source是在hive中已经创建好的数据库名称,
        用于保存原始数据表，
        创建game_info表，用于保存游戏信息。
        """
        hql = """
        CREATE TABLE IF NOT EXISTS source.game_info(fgame_id int, fgame_name string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION '/user/hadoop/source/game_info'
        """
        return self.execute(hql)

    def do_jobs(self):
        """
        从hdfs上导入数据
        """
        hql = """
        LOAD DATA INPATH '/user/hadoop/data/game_info/game_info' INTO TABLE source.game_info
        """
        return self.execute(hql)


if __name__ == "__main__":
    game_info = GameInfo()
    game_info()

