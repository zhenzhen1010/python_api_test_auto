"""
封装requests方法步骤和思路：
1、因为要多次使用，肯定要封装成为函数：def
2、发送接口请求，所以要准备好接口请求四大要素-- 从excel 读取用例数据 可以参数化 形参代替
3、发送接口请求之前，头部和参数需要做反序列操作 转化为字典
4、因为有些接口没有请求头 /没有请求参数，所以在json.loads反序列化之前，要判空
5、发送接口请求之前，接口请求方法有get post put等 各种方法都要支持。
    - 如果是get方法： params接受参数
- 如果是post方法： 根据content-type类型判断用什么接受参数：
  - application/json： json接受参数
  - application/x-www-form-urlencoded： data接受参数
  - multipart/form-data： files接受文件参数
- 如果是put方法
6、文件上传的接口，参数传递有注意事项：
- 如果是上传的接口，一定不要加content-type头部 删除这个头部
- 文件对象： file_obj = {"file":open("tricy.png", "rb")} 不能直接写死在excel里，因为图片要做路径处理 变化的
- 文件路径处理，拼接出来一个动态构造的文件路径
7、函数需要返回值- 接口响应结果
8、加上日志

requests_api方法需要完善：
 - 在发送接口请求之前  应该是做参数和头部的饭序列化之前先完成替换的操作
 - 替换的数据来自于提取存环境变量：调用提取的方法 在接口执行完成之后调用

"""
import json
from config.env import config
import allure
import requests
from tools.handle_path import pic_path
from loguru import logger
from tools.handle_replace import replace_mark
from tools.handle_extract import extract_response
from tools.handle_presql import pre_sql_fun
# 导入加密方法登录
from tools.handle_sign_data import encryto_sign

@allure.step("发送接口请求")
def requests_api(case, token=None, module="excel"):  # 定义token为默认参数
    if module == "excel":
        method = case["请求方法"]
        url = config.data["base_url"] + case["接口地址"]
        param = case["请求参数"]
        header = case["请求头"]
        respond_param = case["提取响应字段"]
        presql_data = None
        try:
            presql_data = case["前置SQL"]
        except Exception as error:
            print(error)
    elif module == "yaml":
        method = case["method"]
        url = config.data["base_url"] + case["url"]
        param = case["param"]
        header = case["header"]
        respond_param = case["extract_data"]
        presql_data = None
        try:
            presql_data = case["presql"]
        except Exception as error:
            print(error)
    # 因为参数里需要调用前置SQL执行的结果 所以要在替换参数之前完成前置SQL的查询操作 : 设置查询结果到环境变量
    if presql_data:
        pre_sql_fun(presql_data)
    # 在发送前以及完成数据替换前调用加密方法
    encryto_sign()
    # 在发送接口请求之前  应该是做参数和头部的饭序列化之前先完成替换的操作  把返回值重新赋值给变量
    param = replace_mark(param)
    header = replace_mark(header)
    url = replace_mark(url)

    # 这里有些用例可能没有请求头和请求参数 所以在反序列化之前做判空处理: 如果头部和参数非空 才做反序列化
    if param is not None:  # 非空判断
        param = json.loads(param)  # 反序列化
    if header is not None:
        header = json.loads(header)  # 反序列化 头部是一个字典
        # if token:  # 非空判断
        #     header["Authorization"] = token  # 给头部新增或者修改键值对 token加上头部里面

    logger.info("==================接口的请求消息============================")
    logger.info(f"请求方法：{method}")
    logger.info(f"请求地址：{url}")
    logger.info(f"请求参数：{param}")
    logger.info(f"请求头部：{header}")

    # 对各种请求方法进行覆盖-- 分支判断
    resp = None  # 初始化这个变量 有默认值 None
    if method.lower() == "get":  # 因为excel表格里可能方法是大写-GET 小写-get 或者大小写结合-Get
        resp = requests.request(method, url, headers=header, params=param)
    elif method.lower() == "post":
        # post请求包括content-type格式类型： json  data  files 三种情况 分别见分支判断的处理
        if header["Content-Type"] == "application/json":
            resp = requests.request(method, url, headers=header, json=param)
        elif header["Content-Type"] == "application/x-www-form-urlencoded":
            resp = requests.request(method, url, headers=header, data=param)
        elif header["Content-Type"] == "multipart/form-data":
            param = {"file": open(pic_path, mode="rb")}  # 图片测试数据的路径处理 导包
            header.pop("Content-Type")  # 文件上传接口不能传content-type头部 否则会报错 所以手动删掉
            logger.info(f"文件参数：{param}")
            logger.info(f"文件的请求头：{header}")
            resp = requests.request(method, url, headers=header, files=param)
    elif method.lower() == "put":
        resp = requests.request(method, url, headers=header, json=param)
    # 设置返回值：响应消息对象
    logger.info("==============================响应消息==========================")
    logger.info(f"响应状态码：{resp.status_code}")
    logger.info(f"响应消息体：{resp.text}")
    # 调用提取的方法 在接口执行完成之后调用
    extract_response(resp, respond_param)
    return resp
