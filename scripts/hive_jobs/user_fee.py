#!/usr/bin/python3

"""
@file: user_fee.py
@brief: 使用hive创建用户付费表并导入数据
@author: feihu1996.cn
@date: 18-08-22
@version: 1.0
"""

from scripts.hive_base import HiveBase


class UserFee(HiveBase):
    """
    使用hive创建用户付费表并导入数据，
    用户付费表变动比较频繁，
    因此，每天都需要导入一次
    """
    def create_table(self):
        """
        hive建表语句,
        source是在hive中已经创建好的数据库名称,
        用于保存原始数据表，
        创建user_fee表，用于保存用户付费信息,
        分区表
        """
        hql = """
        CREATE TABLE IF NOT EXISTS source.user_fee(fdate string, fuser_id int, fgame_id int, ffee int) PARTITIONED BY (dt string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION '/user/hadoop/source/user_fee'
        """
        return self.execute(hql)

    def do_jobs(self):
        """
        从hdfs上导入数据,
        这里将一天的数据作为一个分区导入
        """
        hql = """
        ALTER TABLE source.user_fee ADD IF NOT EXISTS PARTITION (dt='{fdate}') LOCATION '/user/hadoop/data/user_fee/{fdate}'
        """.format(fdate=self.today)
        return self.execute(hql)


if __name__ == "__main__":
    user_fee = UserFee()
    user_fee()

