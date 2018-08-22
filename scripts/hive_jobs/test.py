#!/usr/bin/python3

"""
@file: test.py
@brief: hive统计测试脚本
@author: feihu1996.cn
@date: 18-08-22
@version: 1.0
"""

from scripts.hive_base import HiveBase


class Test(HiveBase):
    """
    hive统计测试
    """
    def create_table(self):
        pass

    def do_jobs(self):
        pass

if __name__ == "__main__":
    test =Test()
    test()

