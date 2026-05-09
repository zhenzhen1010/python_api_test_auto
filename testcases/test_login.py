'''
登录模块的用例执行：
第一步： exec表格里设计好测试用例
第二步： 调用excel表格方法 读取excel文件里用例数据。
第三步： 用pytest编写测试用例 执行测试了 --ddt
第四步： 用requests库发送接口请求了
'''
# 导入excel存放路径文件
import allure

from tools.handle_path import excel_path, yaml_path
# 导入工具库对excel处理
from tools.handle_excel import read_excel
# 导入封装方法处理yaml文件
from tools.handle_yaml import read_yaml
# 引入pytest配置
import pytest
# 引入封装的方法处理断言
from tools.handle_assert import handle_assert
# 引入自行封装的requests
from tools.handle_requests import requests_api

# 第二步 调用excel方法，读取文件数据
# case_all = read_excel(excel_path, "登录")
# 第二步 调用yaml方法，读取文件数据
case_all = read_yaml(yaml_path / "login_data.yaml")


@allure.suite("登录模块")  # 定制化测试套件名字
# @allure.title("{case[用例标题]}")
@allure.title("{case[title]}")  # 添加这行代码就可以把excel用例的标题 作为用例的标题展示
# 第三步 数据驱动执行测试用例
@pytest.mark.parametrize("case", case_all)
@pytest.mark.p0
def test_login_fun(case):
    # excel表测试用例读取数据
    # expected = case["预期结果"]
    # yaml文件测试用例读取数据
    expected = case["assertion"]
    result = requests_api(case, module="yaml")
    # 断言：实际 vs 预期
    # 调用断言封装方法判断断言结果
    handle_assert(result, expected)
