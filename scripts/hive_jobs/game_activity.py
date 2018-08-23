#!/usr/bin/python3

"""
@file: game_activity.py
@brief: hive统计游戏活跃度
@author: feihu1996.cn
@date: 18-08-22
@version: 1.0
"""

from scripts.hive_base import HiveBase


class GameActivity(HiveBase):
    """
    hive统计游戏活跃度
    """
    def create_table(self):
        """
        创建游戏活跃度统计表，
        result是在hive中提前创建好的数据库名称，
        用于保存统计结果表
        """
        hql = """
        CREATE TABLE IF NOT EXISTS result.game_activity (fdate string, fgame_name string, fcount int) partitioned by (dt string) row format delimited fields terminated by ',' location '/user/hadoop/result/game_activity'  
        """
        return self.execute(hql)

    def do_jobs(self):
        """
        统计游戏活跃度，
        并将统计结果插入到游戏活跃度表中
        """
        hql = """
        INSERT OVERWRITE TABLE result.game_activity 
        PARTITION (dt='{fdate}')
        SELECT game_time.fdate, game_info.fgame_name, COUNT(game_time.fuser_id) as fcount FROM source.game_time as game_time left join source.game_info as game_info
        ON game_time.fgame_id=game_info.fgame_id
        WHERE
        game_time.fdate='{fdate}'
        GROUP BY game_info.fgame_name, game_time.fdate 
        """.format(fdate=self.today)
        return self.execute(hql)

if __name__ == "__main__":
    game_activity = GameActivity()
    game_activity()

