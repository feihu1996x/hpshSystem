#!/usr/bin/python3

"""
@file: test.py
@brief: hive统计测试脚本
@author: feihu1996.cn
@date: 18-08-22
@version: 1.0
"""

import random
import datetime
import os

from scripts.hive_base import HiveBase


class Test(HiveBase):
    """
    hive统计测试
    """
    def create_table(self):
        pass

    def do_jobs(self):
        pass


current_work_dir = os.getcwd()

def user_info():
    """
    准备测试数据: 用户信息表    
    """
    areas = ["北京", "上海", "广州", "深圳", "杭州",  "成都", "西安"]
    target_dir = os.getcwd()+"/resource/user_info"
    os.mkdir(target_dir)
    user_file = open(target_dir+"/user_info", "wb")
    for i in range(1000000):
        user_id = str(1000000+i)
        age = str(random.randrange(10, 40))
        area = str(random.choice(areas))
        assets = str(random.randrange(1000, 100000000))
        user_file.write((user_id + "," + age + "," + area + "," + assets + "\n").encode("utf8"))
    user_file.close()

def game_info():
    """
    准备测试数据: 游戏信息表    
    """
    games = ["北京打", "上海斗", "广州跑", "深圳吃", "杭州射", "成都躺", "西安晒"]
    target_dir = os.getcwd()+"/resource/game_info"
    os.mkdir(target_dir)
    game_file = open(target_dir+"/game_info", "wb")
    for i in range(0, len(games)):
        game_id = str(i)
        game_name = str(games[i])
        game_file.write((game_id + "," + game_name + "\n").encode("utf8"))
    game_file.close()

def game_time():
    """
    准备测试数据：游戏时间表，
    哪一天哪个用户在哪个游戏中玩了多长时间
    """
    game_ids = [0, 1, 2, 3, 4, 5, 6]
    for j in range(10):
        date = (datetime.datetime.now()+datetime.timedelta(days=j)).strftime("%Y-%m-%d")
        target_dir = os.getcwd()+"/resource/game_time/"+date
        os.system("mkdir -p {target_dir}".format(target_dir=target_dir))
        time_file = open(target_dir+"/game_time", "wb")
        for i in range(1000000):
            fdate = str(date)
            user_id = str(1000000+i)
            game_id = str(random.choice(game_ids))
            game_time = str(random.randrange(10, 60))
            time_file.write((date + "," + user_id + "," + game_id + "," + game_time + "\n").encode("utf8"))
        time_file.close()

def user_fee():
    """
    准备测试数据：用户付费表，
    哪一天哪个用户在哪个游戏中花了多少钱
    """
    game_ids = [0, 1, 2, 3, 4, 5, 6]
    for j in range(10):
        date = (datetime.datetime.now()+datetime.timedelta(days=j)).strftime("%Y-%m-%d")
        target_dir = os.getcwd()+"/resource/user_fee/"+date
        os.system("mkdir -p {target_dir}".format(target_dir=target_dir))
        fee_file = open(target_dir+"/user_fee", "wb")
        for i in range(1000000):
            fdate = str(date)
            user_id = str(1000000+i)
            game_id = str(random.choice(game_ids))
            fee = str(random.randrange(10, 1000))
            fee_file.write((date + "," + user_id + "," + game_id + "," + fee + "\n").encode("utf8"))
        fee_file.close()

# user_info()
# game_info()
# game_time()
# user_fee()

# test =Test()
# test()

