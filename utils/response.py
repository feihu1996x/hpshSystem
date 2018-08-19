#!/usr/bin/python3

"""
@file: response.py
@brief: 数据响应类
@author: feihu1996.cn
@date: 18-08-19
@version: 1.0
"""

class Status:
    """
    响应状态码    
    """
    SUCCESS = 0
    ERROR = 1


class Response(Status):
    """
    数据响应类    
    """
    @classmethod
    def responseJson(cls, code=0, data=[], msg=""):
        """
        JSON响应
        """
        msg_dict = {
            cls.SUCCESS: "请求成功",
            cls.ERROR: "请求失败"
        }
        if not msg:
            msg = msg_dict.get(code, "未定义信息")
        res ={
            "code": code,
            "msg": msg,
            "data": data
        }
        return res

    @classmethod
    def responseHtml(cls, data=None):
        """
        HTML响应    
        """
        pass

if __name__ == "__main__":
    print(Response.responseJson(code=Response.SUCCESS, data=[{"a":1}]))

