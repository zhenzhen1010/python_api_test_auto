"""
1、get请求的接口：
 - 参数的接受用 params关键字接受
2、在用例代码里直接写的参数和头部的反序列化操作 所以如果excel里参数和头部为空  会报错吗？

"""
import allure
import pytest
from tools.handle_excel import read_excel
from tools.handle_path import excel_path
from tools.handle_assert import handle_assert
from tools.handle_requests import requests_api

# 第二步： 调用excel表格方法 读取excel文件里用例数据。用一个变量接受返回值
case_all = read_excel(excel_path,"搜索")
@allure.title("{case[用例标题]}")
# 第三步： 用pytest编写测试用例 执行测试了 --ddt
@pytest.mark.parametrize("case",case_all)
def test_search_case(case):
    resp = requests_api(case)
    # 断言
    expeceted_result = case["预期结果"]
    handle_assert(resp, expeceted_result)
