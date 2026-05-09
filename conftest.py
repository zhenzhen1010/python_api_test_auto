'''
定义请求执行夹具
应用场景：
    例如登录：先做登录，拿到对应的token，再执行后续代码
'''
import pytest
# import requests
from tools.handle_requests_bak import Requests
from jsonpath import jsonpath
from config.env import config

requests = Requests()


# 调用钩子函数pytest_addoption，自定义命令行参数
def pytest_addoption(parser):
    # 注册⾃定义参数命令⾏参数
    parser.addoption("--env", default="test", choices=['dev', 'test', 'pre', 'prod'], help="命令⾏参数'--env'设置环境切换")


# 定义夹具，处理环境配置的切换
@pytest.fixture(scope="session", autouse=True)
def get_env(request):
    # 从命令行中获取env配置
    env_name = request.config.getoption("--env")
    # 调用配置文件加载对应的环境配置
    config.load(env_name)


# 登录夹具
@pytest.fixture
def login_fixture():
    url = "http://shop.lemonban.com:8107/login"
    post_method = "POST"
    param = {"principal": "13560088365", "credentials": "123456", "appType": 3, "loginType": 0}
    header = {"Accept-Language": "zh"}
    res = requests.post(url, header=header, param=param)
    # print(res.text)
    login_token = jsonpath(res.json(), "$..access_token")[0]
    # print(f"login_token:-----{login_token}")
    yield 'bearer' + login_token
