#!/usr/bin/python3

"""
@file: sql_tpl.py
@brief: SQL语句模板
@author: feihu1996.cn
@date: 18-08-20
@version: 1.0
"""

SQL_TPL = {
    "game_activity": """
                SELECT fdate, COUNT(fgame_id) AS game_activity FROM game_activity WHERE fdate>='{start_date}' AND fdate <='{end_date}' GROUP BY fdate;
              """
}

