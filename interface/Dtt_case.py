#coding:utf-8
__author__ = "langtuteng"
import unittest
from ddt import ddt,data,file_data,unpack
from public.excel_oparete import makedata,BASE_DIR
from interface import testapi
import os

path = os.path.join(BASE_DIR,'testCase/case.xlsx')
res = makedata(path)
@ddt
class Ddt_case(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*res)
    def test_ddt(self,res):
        tapi = testapi.TestApi(id = res["id"],paras = res["paras"],url = res["url"],method = res["method"],hope = res["hope"])
        result = tapi.getresult()
        print(result)



if __name__ == '__main__':
    unittest.main()


