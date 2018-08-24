#!/usr/bin/env python3

"""
@file: begin.py
@brief: begin this project
@author: feihu1996.cn
@date: 18-08-24
@version: 1.0
"""

import sys
import os
import re

from models.data_model import DataModel

work_dir = os.getcwd()


if len(sys.argv) < 2:
    # 启动web app
    print("启动web app...")
    gun_file = open("gun.conf", "rb")
    temps = []
    for line in gun_file.readlines():
        if "chdir" not in line.decode("utf8"):
            temps.append(line)
    gun_file.close()
    gun_file = open("gun.conf", "wb")
    gun_file.writelines(temps)
    gun_file.close()
    os.system(r"""
    echo chdir = \'{work_dir}\' >> gun.conf
    """.format(work_dir=work_dir))
    os.system(r"""
    gunicorn -k gevent -c gun.conf bootstrap:app
    """)
elif "init" == sys.argv[1]:
    # 准备测试数据
    print("准备测试数据...")
    
    model = DataModel()
    import datetime
    import random

    # 游戏活跃度数据
    insert_sql = "INSERT INTO game_activity(fdate, fgame_name, fcount) VALUES "
    sql_list = []
    game_list = ["北京打", "上海斗", "广州跑", "深圳吃", "杭州射", "成都躺", "西安晒"]
    for j in range(0, 100):
        fdate = (datetime.datetime.now().date() + datetime.timedelta(days=j)).strftime("%Y-%m-%d")
        for game in game_list:
            fgame_name = game
            fcount = random.randrange(100, 1000)
            sql = "('{}', '{}', {})".format(fdate, fgame_name, fcount)
            sql_list.append(sql)
    insert_sql += ','.join(sql_list) 
    print(model.mysql_db.execute_commit(insert_sql))   
elif "prepare" == sys.argv[1]:
    # 准备使用Hive进行大数据统计需要的结构化数据
    print("准备使用Hive进行大数据统计需要的结构化数据...")

    os.system("mkdir -p resource")

    from scripts.hive_jobs.test import user_info, \
                                       game_info, \
                                       game_time, \
                                       user_fee   
    user_info()
    game_info()
    game_time()
    user_fee() 

    from scp import SCPClient
    from scripts.sqoop_base import SqoopBase
    
    sqoop_base = SqoopBase()

    sqoop_base.execute("mkdir -p /home/hadoop/data")

    scp = SCPClient(sqoop_base.ssh.get_transport())

    scp.put(files=["resource/user_info", "resource/game_info", "resource/game_time", "resource/user_fee"], remote_path='/home/hadoop/data', recursive=True) 

    scp.close()
    
    sqoop_base.execute("""
    hdfs dfs -put ~/data /user/hadoop 
    """)
    
    os.system("rm -rf resource")
elif "hive" == sys.argv[1]:
    print("使用Hive进行大数据统计")

    from scripts.hive_jobs.user_info import UserInfo
    from scripts.hive_jobs.user_fee import UserFee
    from scripts.hive_jobs.game_time import GameTime
    from scripts.hive_jobs.game_info import GameInfo
    from scripts.hive_jobs.game_activity import GameActivity
    from scripts.hive_jobs.game_user_age import GameUserAge

    UserInfo()()
    UserFee()()
    GameTime()()
    GameInfo()()
    GameActivity()()
    GameUserAge()() 
elif "sqoop" == sys.argv[1]:
    print("使用Sqoop将数据导出到MySQL")
   
    from scripts.sqoop_jobs.game_activity import GameActivity
    from scripts.sqoop_jobs.game_activity import GameUserAge

    GameActivity()()
    GameUserAge()() 
     
