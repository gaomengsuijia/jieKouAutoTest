#coding:utf-8
__author__ = "langtuteng"

import requests
import json


class Jiekou_request(object):
    '''
    封装get和post请求
    '''
    def __init__(self):
        self.headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    def post_json(self,url,data):
        '''
        发送json
        :param url:
        :param data:
        :return:
        '''
        data = json.dumps(data)
        try:
            result = requests.post(url=url,data=data,headers=self.headers)
            result.raise_for_status()
            return result.text
        except requests.RequestException as e:
            print(str(e))



    def post(self,url,data):
        '''
        post请求
        :param url:
        :param data:
        :return:
        '''
        # data = json.dumps(data)
        try:
            # result = requests.post(url=url,data=data,headers=self.headers)
            result = requests.post(url=url, data=data)
            result.raise_for_status()
            return result.text
        except requests.RequestException as e:
            print(str(e))


    def get(self,url,params):
        '''
        get请求
        :param url:
        :param params:
        :return:
        '''
        try:
            result = requests.get(url=url,params=params)
            result.raise_for_status()#如果状态码不是200，主动抛出异常
            return result.text
        except requests.RequestException as e:
            print(str(e))



if __name__ == '__main__':
    jiekou = Jiekou_request()