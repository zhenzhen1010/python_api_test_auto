from loguru import logger
import json
from jsonpath import jsonpath
from data.envi_data import EnviData

# 调用方法设置对key和value值
def extract_response(resp, excel_data):
    '''
    :param res: 响应体返回值
    :param excel_data: excel 读取的提取值字段
    '''
    # 如果没有提取值则不往下执行
    if excel_data is None:
        logger.info("------不需要作提取处理------")
        return
    # 反序列化excel取到的值
    if type(excel_data) == str:
        excel_data = json.loads(excel_data)
    # print(excel_data_dict.items())
    # for 循环读取要提取的字段
    for k, v in excel_data.items():
        logger.info(f"需要作提取处理Key：{k}")
        # jsonpath(json_text, "$..actualTotal")[0]
        value = None
        if v.startswith("$"):
            value = jsonpath(resp.json(), v)[0]
        elif v == "text":
            value = resp.text  # 获取响应结果的text文本信息
        logger.info(f"需要作提取处理Value：{value}")
        # 把提取到的key和value保存到环境变量EnviData对象中
        setattr(EnviData, k, value)
    # 读取环境变量EnviData的属性
    logger.info(f"设置到环境变量类的值{EnviData.__dict__}")
    # print(EnviData.__dict__)

