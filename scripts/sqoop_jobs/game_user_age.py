#!/usr/bin/python3

"""
@file: game_user_age.py
@brief: sqoop导出游戏用户年龄段数据
@author: feihu1996.cn
@date: 18-08-24
@version: 1.0
"""

from scripts.hive_base import SqoopBase


class GameUserAge(SqoopBase):
    """
    sqoop导出游戏用户年龄段数据
    """
    def create_table(self):
       sql = """
       CREATE TABLE IF NOT EXISTS game_user_age (fdate VARCHAR(64), fgame_time INT, fage INT) CHARACTER SET utf8mb4
       """ 
        return self.mysql_db.execute_commit(sql)

    def sqoop_jobs(self):
        cmd = """
        sqoop export \
        --connect jdbc:mysql://{mysql_host}:{mysql_port}/{mysql_database}?characterEncoding=utf8 \
        --username {mysql_user} \
        --password "{mysql_password}" \
        --table game_user_age \
        -m 1 \
        --export-dir /user/hadoop/result/game_user_age/dt={fdate} \
        --fields-terminated-by ','
        """.format(mysql_host=self.mysql_host, mysql_port=self.mysql_port, mysql_database=self.mysql_database, mysql_user=self.mysql_user, mysql_password=self.mysql_password, fdate=self.today)        
        self.execute(cmd)


if __name__ == "__main__":
    game_user_age = GameUserAge()
    game_user_age()

