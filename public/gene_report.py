#coding:utf-8
__author__ = "langtuteng"
from lib import HTMLTestRunner
import time
import os
BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR,'test_report')
def gene_report(suite):
    '''
    生成测试报告
    :param suite:
    :return:
    '''
    file_name = os.path.join(file_path,(time.strftime('%Y-%m%d',time.gmtime()) + '.html'))

    with open(file_name,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,title="接口测试报告",description="接口测试"
        )
        runner.run(suite)

