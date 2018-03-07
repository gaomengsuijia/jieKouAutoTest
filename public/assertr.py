#coding:utf-8
__author__ = "langtuteng"
import unittest
from public.log import print_log
def assertcode(hope):
    '''
    断言，获取接口测试用例的hope值
    :param hope:
    :return:
    '''
    lis = hope.split("&")
    if len(lis)>0:
        result = dict([(item.split("=")) for item in lis])
        return result


    else:
        print_log.warn("hope值非法格式")
        raise Exception("hope值非法格式")


