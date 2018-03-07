#coding:utf-8
__author__ = "langtuteng"
import time
from public.log import print_log
import os
from functools import wraps
def genelog():
    '''
    生成日志
    :return:
    '''
    path = os.path.join("logs\\",(time.strftime("%Y-%m%d",time.gmtime()) + '.log'))
    return print_log(path)

printlog = genelog()

def prinwrap(para):
    '''
    装饰器
    derocator
    :param para:
    :return:
    '''
    def wraper(func):
        @wraps(func)
        def _wraper(*args,**kwargs):
            printlog.debug('当前模块名称--{}'.format(para))
            fun = func(*args,**kwargs)
            return fun
        return _wraper

    return wraper
