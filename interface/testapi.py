#coding:utf-8
__author__ = "langtuteng"
from public import jiekou_request
from public.gene_log import prinwrap,printlog

class TestApi(object):
    '''
    接口请求
    '''

    def __init__(self,id,paras,url,method,hope):
        self.id = id
        self.paras = paras
        self.url = url
        self.method = method
        self.hope = hope
        self.jiekou_req = jiekou_request.Jiekou_request()


    def gene_para_dict(self):
        '''
        将字符串形式的参数，转化为字典形式
        :return:
        '''
        data = {}
        para_list = self.paras.split("&")
        for each in para_list:
            if each != "":
                data[each.split("=")[0].strip()] = each.split("=")[1].strip()

        return data


    def testapi(self):
        '''

        :return:
        '''
        printlog.info("开始调用接口测试用例id-{}".format(self.id))
        data = self.gene_para_dict()
        print(data)
        if self.method == "POST":
            test = self.jiekou_req.post(url=self.url,data=data)
        elif self.method == "GET":
            test = self.jiekou_req.get(url=self.url,params = data)
        else:
            raise Exception("接口请求方式不正确")

        return test

    @prinwrap("接口发送请求")
    def getresult(self):
        '''
        获取接口的实际返回值
        :return:
        '''
        result = self.testapi()
        printlog.info("接口返回数据：{}".format(result))
        return result


