## hpshSystem

## 项目描述

简易大数据统计与可视化系统

## 技术栈

HTML

CSS 

JavaScript

Echarts(数据可视化)

Flask(Web后端)

Python

MySQL

MongoDB(请求数据缓存, 体积较大的数据)

Redis(请求数据缓存)

Hadoop

Hive(海量数据处理与统计)

Sqoop(HDFS分布式文件系统与关系数据库之间数据互导)

Supervisor(进程管理)

Crontab(定时调度)

Nginx(反向代理)

docker(应用容器)

## Build and Setup

```bash

# 安装依赖
pip install -r requirements.txt

# 导入数据库
mysql -uroot -p hpshSystem < hpshSystem.sql

# 准备测试数据
python3 begin.py init

# 启动Web App
python3 begin.py

# 准备使用Hive进行大数据统计需要的结构化数据
python3 begin.py prepare

# 使用Hive进行大数据统计
python3 begin.py hive

# 使用Sqoop将数据导出到MySQL
python3 begin.py sqoop

```

