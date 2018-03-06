#coding:utf-8
__author__ = "langtuteng"
import logging

class print_log(object):
    '''
    封装日志类
    '''

    def __init__(self,path):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


        #设置文件日志
        fl = logging.FileHandler(path)
        fl.setLevel(logging.DEBUG)
        fl.setFormatter(formatter)

        #设置cmd日志

        stl = logging.StreamHandler()
        stl.setLevel(logging.DEBUG)
        stl.setFormatter(formatter)

        #添加handle

        self.logger.addHandler(fl)
        self.logger.addHandler(stl)


    def debug(self,message):
        self.logger.debug(message)


    def error(self,message):
        self.logger.error(message)


    def info(self,message):
        self.logger.info(message)


    def warn(self,message):
        self.logger.info(message)




if __name__ == '__main__':
    printlog = print_log('debug.log')
    printlog.debug("debug message")
    printlog.error("error message")
    printlog.info("info message")
    printlog.warn("warn messge")
