# hpshSystem

> 大数据统计与可视化系统

## Tech Stack

- HTML/CSS/JavaScript
- Echarts
- Flask
- Python
- MySQL
- MongoDB
- Redis
- Hadoop/HDFS/Hive/Sqoop
- Crontab
- Nginx
- Docker
- Gunicorn
- Supervisor

## Build and Setup

```bash
# 安装依赖库
yum install gcc-c++ \
python-devel.x86_64 \
cyrus-sasl-lib.x86_64 \
cyrus-sasl-devel.x86_64 \
libgsasl-devel.x86_64 -y
pip3 install -r requirements.txt

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

# 清除MongoDB缓存
python3 begin.py nocache
```

## Demo Link

[http://dev.feihu1996.cn/hpshsystem/](http://dev.feihu1996.cn/hpshsystem/ "hpshSystem")
