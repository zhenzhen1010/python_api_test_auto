'''
http请求封装
    -get 请求：实例方法，通过实例对象.调用
    -post  请求
'''
# 引入requests包
import requests
from tools.handle_extract import extract_response
# 日志
from loguru import logger


class Requests:
    baseUrl = ""

    def get(self, url, case, header={}, param={}):
        '''
        :param case:
        :param url: 请求地址（除公共部分，即从端口后开始）
        :param header: 请求头信息-默认{}
        :param param: 请求参数-默认{}
        :return: 返回响应结果
        '''
        logger.info("=================Get请求执行========================")
        logger.info(f"请求URL：{self.baseUrl + url}")
        logger.info(f"请求header：{header}")
        logger.info(f"请求param：{param}")
        resp = requests.request("GET", self.baseUrl + url, headers=header, params=param)
        logger.info(f"Get响应结果：{resp.text}")

        if case:
            # 提取值到环境变量中去
            extract_response(resp, case["提取响应字段"])
        return resp

    def post(self, url, case, header={}, param={}):
        '''
        :param case:
        :param url:请求地址（除公共部分，即从端口后开始）
        :param header:求头信息-默认{}
        :param param:请求参数-默认{}
        :return:返回响应结果
        '''
        logger.info("=================Post请求执行========================")
        logger.info(f"请求URL：{self.baseUrl + url}")
        logger.info(f"请求header：{header}")
        logger.info(f"请求param：{param}")
        # 获取Content-Type类型
        contentType = header.get('Content-Type')
        url = self.baseUrl + url
        resp = ""
        if contentType == "application/x-www-form-urlencoded":
            logger.info(f"进入x-www-form-urlencoded模式请求，contentType：{contentType}")
            resp = requests.request("POST", url, headers=header, data=param)
        elif contentType == "multipart/form-data":
            logger.info(f"进入form-data模式请求，contentType：{contentType}")
            # 一定要去掉content-type 不然会报错
            header.pop("Content-Type")
            resp = requests.request("POST", url, headers=header, files=param)
        else:
            logger.info(f"进入application/json模式请求，contentType：{contentType}")
            resp = requests.request("POST", url, headers=header, json=param)

        logger.info(f"Post响应结果：{resp.text}")

        if case:
            # 提取值到环境变量中去
            extract_response(resp, case["提取响应字段"])

        return resp

    def put(self, url, case, header={}, param={}):
        '''
            :param case:
            :param url:请求地址（除公共部分，即从端口后开始）
            :param header:求头信息-默认{}
            :param param:请求参数-默认{}
            :return:返回响应结果
        '''
