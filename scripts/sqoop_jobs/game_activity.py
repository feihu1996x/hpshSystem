#!/usr/bin/python3

"""
@file: game_activity.py
@brief: sqoop导出游戏活跃度数据
@author: feihu1996.cn
@date: 18-08-24
@version: 1.0
"""

from scripts.sqoop_base import SqoopBase


class GameActivity(SqoopBase):
    """
    sqoop导出游戏活跃度数据
    """
    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS game_activity (fdate VARCHAR(64), fgame_name VARCHAR(64), fcount INT) CHARACTER SET utf8mb4 
        """
        return self.mysql_db.execute_commit(sql) 

    def sqoop_jobs(self):
        cmd = """
        sqoop export \
        --connect jdbc:mysql://{mysql_host}:{mysql_port}/{mysql_database}?characterEncoding=utf8 \
        --username {mysql_user} \
        --password "{mysql_password}" \
        --table game_activity \
        -m 1 \
        --export-dir /user/hadoop/result/game_activity/dt={fdate} \
        --fields-terminated-by ','
        """.format(mysql_host=self.mysql_host, mysql_port=self.mysql_port, mysql_database=self.mysql_database, mysql_user=self.mysql_user, mysql_password=self.mysql_password, fdate=self.today)        
        self.execute(cmd)
                 

if __name__ == "__main__":
    game_activity = GameActivity()
    game_activity()

