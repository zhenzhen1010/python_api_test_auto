'''
上传文件模块的用例执行：
第一步： exec表格里设计好测试用例
第二步： 调用excel表格方法 读取excel文件里用例数据。
第三步： 用pytest编写测试用例 执行测试了 --ddt
第四步： 用requests库发送接口请求了
'''
# 导入excel存放路径文件
import allure

from tools.handle_path import excel_path
# 导入工具库对excel处理
from tools.handle_excel import read_excel
# 引入requests包
# import requests
# 引入内置函数
import json
# 引入pytest配置
import pytest
# 引入封装的方法处理断言
from tools.handle_assert import handle_assert
# 引入自行封装的requests
from tools.handle_requests import requests_api
# 引入测试图片路径
from tools.handle_path import pic_path
from tools.handle_replace import replace_mark

# 第二步 调用excel方法，读取文件数据
case_all = read_excel(excel_path, "上传")
print(case_all)
# 创建Requests请求实例
# requests = Requests()

@allure.title("{case[用例标题]}")
# 第三步 数据驱动执行测试用例
@pytest.mark.parametrize("case", case_all)
# def test_upload_fun(case, login_fixture):  # 调用夹具
def test_upload_fun(case):
    expected = case["预期结果"]
    result = requests_api(case)
    print(result.text)
    # 调用断言封装方法判断断言结果
    handle_assert(result, expected)
#
