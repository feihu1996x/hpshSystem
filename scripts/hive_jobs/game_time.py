#!/usr/bin/python3

"""
@file: game_time.py
@brief: 使用hive创建游戏时间表并导入数据
@author: feihu1996.cn
@date: 18-08-22
@version: 1.0
"""

from scripts.hive_base import HiveBase


class GameTime(HiveBase):
    """
    使用hive创建游戏时间表并导入数据，
    游戏时间表变动比较频繁，
    因此，每天都需要导入一次
    """
    def create_table(self):
        """
        hive建表语句,
        source是在hive中已经创建好的数据库名称,
        用于保存原始数据表，
        创建game_time表，用于保存游戏时间信息,
        分区表
        """
        hql = """
        CREATE TABLE IF NOT EXISTS source.game_time(fdate string, fuser_id int, fgame_id int, fgame_time int) PARTITIONED BY (dt string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION '/user/hadoop/source/game_time'
        """
        return self.execute(hql)

    def do_jobs(self):
        """
        从hdfs上导入数据,
        这里将一天的数据作为一个分区导入
        """
        hql = """
        ALTER TABLE source.game_time ADD IF NOT EXISTS PARTITION (dt='{fdate}') LOCATION '/user/hadoop/data/game_time/{fdate}'
        """.format(fdate=self.today)
        return self.execute(hql)


if __name__ == "__main__":
    game_time = GameTime()
    game_time()

