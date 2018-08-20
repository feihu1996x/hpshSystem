#!/usr/bin/python3

"""
@file: data_controller.py
@brief: 数据控制器
@author: feihu1996.cn
@date: 18-08-20
@version: 1.0
"""

from collections import defaultdict

from utils.response import Response
from utils.items import item_dict
from utils.logger import Logger
from controllers.base_controller import BaseController
from models.data_model import DataModel
from models.user_model import UserModel
from models.auth_model import AuthModel


class DataController(BaseController):
    """
    数据控制器
    """
    def __init__(self, *args, **kwargs):
        super(DataController, self).__init__(*args, **kwargs)
        self.data = DataModel()
        self.user = UserModel()
        self.auth = AuthModel()

    def get_data(self):
        """
        获取图表数据
        """
        dims = self.args.get('dims', None)
        if not dims:
            return Response.responseJson(Response.INPUT_EMPTY, msg="输入指标为空")

        # 验证用户是否有权限查看当前指标数据
        isAuth = self.auth_require(dims_name=dims)
        Logger.debug_logger().debug(isAuth)
        if not isAuth:
            return Response.responseJson(Response.NO_AUTH)

        params = {
            "start_date": self.args.get("start_date", ""),
            "end_date": self.args.get("end_date", "")
        }

        # 调用模型方法获取数据
        results = self.data.get_data(dims=dims, args=params)

        print(results)

        # 格式化数据
        option = {
            "name": dims,
            "type": "bar",
            "data": results,
            "title": item_dict.get(dims, dims)
        }
        results = self.format_data(option=option)

        #option = {
        #    "title": "hpshSystem",
        #    "xAxis": ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],
        #    "series": [{
        #        "name": '销量',
        #        "data": [5, 20, 36, 10, 10, 20]
        #    }]        
        #}

        return Response.responseJson(Response.SUCCESS, data=results, msg="获取数据成功")

    def format_data(self, option=None):
        """
        格式化数据
        """
        data = option.get("data", [])
        name = option.get("name", "")
        e_type = option.get("type", "bar")
        title = option.get("title", name)

        dict_data = defaultdict(list)
        for item in data:
            key = item.get("fdate", None)
            dict_data[key].append(item.get(name))

        # 对dict_data进行升序排序
        dict_data = sorted(dict_data.items(), key=lambda x: x[0], reverse=False)

        axis_x = []
        axis_y = []

        for key, obj in dict_data:
            axis_x.append(key)
            axis_y.append(sum([item for item in obj if isinstance(item, (float, int))]))

        results = {
            "xAxis": axis_x,
            "title": title,
            "series": [{
                "name": name,
                "data": axis_y,
                "type": e_type
            }]
        }

        return results

    def auth_require(self, dims_name=None):
        """
            根据用户级别控制其可以查看的指标数据    
        """
        # 获取用户工号、等级信息
        fwork_id = self.session.get("fwork_id", None)
        user_info = self.user.get_user_info(fwork_id=fwork_id)
        flevel_id = user_info.get("flevel_id", 0)

        # 获取指标的等级要求信息
        auth_level = self.auth.get_auth_level(dims_name=dims_name)
        auth_level_id = auth_level.get("flevel_id", 100000)

        # 比较是否有权限
        if flevel_id < auth_level_id:
            return False

        return True

