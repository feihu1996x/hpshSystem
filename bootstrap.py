#!/usr/bin/python3

"""
@file: bootstrap.py
@brief: 项目入口文件
@author: feihu1996.cn
@date: 18-08-17
@version: 1.0
"""

from flask import Flask, g, request, render_template, session

from views.users import user
from utils.logger import Logger


app = Flask(__name__)

app.config.from_pyfile("config.py")

BLUEPRINT= [user]


@app.context_processor
def common():
    return {
        "isLogin": True if session.get("fwork_id", None) else False
    }

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

def bootstrap(app=None):
    for view in BLUEPRINT:  # 注册蓝图
        app.register_blueprint(view)
    
    # 中间件
    @app.before_request
    def before():
        # 获取所有请求参数(get和post)
        # 保存到全局变量g中
        args_get = {k: v[0] for k, v in dict(request.args).items()}
        args_post = {k: v[0] for k, v in dict(request.form).items()}
        args_get.update(args_post)
        g.request_args = args_get

bootstrap(app)


if __name__ == "__main__":
    Logger.info_logger().info('starting -- {} -- {}'.format(app.config['WEB_HOST'], app.config['WEB_PORT']))
    app.run(host=app.config["WEB_HOST"], port=app.config["WEB_PORT"])

