#!/usr/bin/python3

"""
@file: bytes_to_str_dict.py
@brief: bytes字典转str字典
@author: feihu1996.cn
@date: 18-08-20
@version: 1.0
"""

def bytes_to_str_dict(data):
    """
    bytes字典转str字典    
    """
    result_dict = {}
    for k,v in data.items():
        k = k.decode()
        v = v.decode()
        result_dict.setdefault(k, v)
    return result_dict


if __name__ == "__main__":
    data = {b'fname': b'\xe7\xab\xa0\xe4\xb8\x89', b'fwork_id': b'1001', b'fdept_id': b'1', b'flevel_id': b'1'}
    data = bytes_to_str_dict(data)
    print(data)

