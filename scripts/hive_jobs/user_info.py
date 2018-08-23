#!/usr/bin/python3

"""
@file: user_info.py
@brief: 使用hive创建用户信息表并导入数据
@author: feihu1996.cn
@date: 18-08-22
@version: 1.0
"""

from scripts.hive_base import HiveBase


class UserInfo(HiveBase):
    """
    使用hive创建用户信息表并导入数据
    """
    def create_table(self):
        """
        hive建表语句,
        source是在hive中已经创建好的数据库名称,
        创建user_info表，用于保存用户信息.
        """
        hql = """CREATE TABLE IF NOT EXISTS source.user_info(fuser_id int, fage int, farea string, fasset int) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION '/user/hadoop/source/user_info'"""
        return self.execute(hql)

    def do_jobs(self):
        """
        从hdfs上导入数据
        """
        hql = """LOAD DATA INPATH '/user/hadoop/data/user_info/user_info' INTO TABLE source.user_info"""
        return self.execute(hql)


if __name__ == "__main__":
    user_info = UserInfo()
    user_info()

