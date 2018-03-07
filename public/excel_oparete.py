#coding:utf-8
__author__ = "langtuteng"
import openpyxl
import os
BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class excel_oparete(object):
    def __init__(self,path):
        self.path = path


    def __call__(self):
        return self.get_data()


    def get_data(self):
        '''
        获取每行的数据
        :return:
        '''
        id = []
        paras = []
        url = []
        method = []
        hope = []
        result = []
        wb = openpyxl.load_workbook(self.path)
        #获取工作表
        st = wb["Sheet1"]
        for each_row in st.rows:
            id.append(each_row[0].value)
            paras.append(each_row[2].value)
            url.append(each_row[3].value)
            method.append(each_row[4].value)
            hope.append(each_row[5].value)
            result.append(each_row[6].value)
        return id,paras,url,method,hope,result


def makedata(path):
    '''
    数据封装成每一条用例
    :param data:
    :return:
    '''
    data = excel_oparete(path)
    id,paras,url,method,hope,result = data()
    res = []
    for i in range(1,len(id)):
        res.append({"id":id[i],"paras":paras[i],"url":url[i],
                    "method":method[i],"hope":hope[i],"result":result[i]
                    })
    return res





if __name__ == '__main__':
    path = os.path.join(BASE_DIR,'testCase/case.xlsx')
    # excel = excel_oparete(path)
    # data = excel.get_data()
    # print(data)
    res = makedata(path)
    print(res)