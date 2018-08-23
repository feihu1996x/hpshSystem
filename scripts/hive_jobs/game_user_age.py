#!/usr/bin/python3

"""
@file: game_user_age.py
@brief: 统计游戏用户年龄段
@author: feihu1996.cn
@date: 18-08-22
@version: 1.0
"""

from scripts.hive_base import HiveBase


class GameUserAge(HiveBase):
    """
    hive统计游戏用户年龄段
    """
    def create_table(self):
        """
        创建游戏用户年龄段统计表，
        result是在hive中提前创建好的数据库名称，
        用于保存统计结果表
        """
        hql = """
        CREATE TABLE IF NOT EXISTS result.game_user_age (fdate string, fgame_time int, fage int)
        PARTITIONED BY (dt string)
        ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
        LOCATION '/user/hadoop/result/game_user_age'
        """
        return self.execute(hql)

    def do_jobs(self):
        """
        统计游戏用户年龄段，
        并将统计结果插入到游戏用户年龄段统计表中
        """
        hql = """
        INSERT OVERWRITE TABLE result.game_user_age
        PARTITION (dt='{fdate}')
        SELECT game_time.fdate as fdate, SUM(game_time.fgame_time) AS fgame_time, user_info.fage as fage FROM source.game_time AS game_time
        LEFT JOIN source.user_info AS user_info
        ON game_time.fuser_id=user_info.fuser_id
        WHERE game_time.fdate = '{fdate}'
        GROUP BY user_info.fage, game_time.fdate
        """.format(fdate=self.today)
        return self.execute(hql)

if __name__ == "__main__":
    game_user_age = GameUserAge()
    game_user_age()

