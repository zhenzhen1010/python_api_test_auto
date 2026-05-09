'''
断言结果处理
1、用例一定要加上断言 才能只能通过相信真的通过
2、断言最好选择一个字段做断言：
   - 字段一定要唯一标识这个结果是否通过  + 字段的是确定 不是每次会变化
   比如登录通过的用例: "nickName":"lemon_python","enabled":true
3、预期结果是 lemon_python  ,执行结果： 要去登录结果里提取
   - 问题： 如何从登录的结果提取nickname的值  enabled的值 作为执行结果？--jsonpath提取
   - 断言： assert 执行结果 == 预期结果
4、但是这个断言的代码不能直接写到pytest的用例去：
  - 因为每条用例的断言预期和执行结果不一样的 ： 登录第一条是json结果，后面用例是文本
  - 测试数据变化的： lemon_python用户名是变化的数据 每个人写的脚本都会不一样 变化的数据跟测试用例设计的数据有关 不要写代码里
     最好写好excel表里。
  所以: 断言每条用例不一样，而且每个数据可能不一样，所以跟着用例走 放在excel里写。
5、写到excel预期结果 这一列里实现：
  - "$..nickName"  --这个是跟用例相关的 不同执行不一样  jsonpath提取表达式不一样的
  - "lemon_python" 这个测试数据 预期结果 也是变化的
  设计： json格式  {"$..nickName":"lemon_python"}  --key:提取表达式，value：预期结果

6、代码处理断言的思路：
  -第一步： 代码读取excel里预期结果这一列的数据： '{"$..nickName":"lemon_python"}'
     - 得到key 和value ： key用来从响应结果做提取数据的  value用来做断言
  - 第二步：因为需要for循环遍历这个字典 所以先把json串 转化为字典 --反序列化
  - 第三步: 分别得到字典的key和value for循环遍历

7、登录用例里第一条是json后面的都是文本： 不能用jsonpath提取
  - 文本可以只用用resp.text 获取文本 -- 就是执行结果
  - excel里设计： {"text":"账号或密码不正确"}

8、代码逻辑里要做分支判断 根据读取预期结果excel数据做判断：
  - 如果k ==text ： 做文本提取  做断言
  - 如果k 是json提取表达式，那么做json提取 做断言
    - jsonpath表达式是$ 开头： startswith("$")
'''
# 引入jsonpath取值工具库
import json
# jsonpath 获取数据
import allure
from jsonpath import jsonpath
# 日志
from loguru import logger
from tools.handle_replace import replace_mark

@allure.step("做响应断言")
def handle_assert(result, expected_data):
    logger.info("--------开始响应断言---------")
    if expected_data is None:
        logger.info("这条用例不需要断言！直接返回通过")
        return  # 直接函数的返回  不执行后面断言代码
    # 替换变量
    expected_data = replace_mark(expected_data)
    expected_data = json.loads(expected_data)
    logger.info(f"期望结果的表达式是：{expected_data}")
    for k, v in expected_data.items():
        # 需要对k做判断
        if k == "text":
            try:
                assert result.text == v
                logger.info(f"用例执行结果：{result.text}")
                logger.info(f"用例预期结果：{v}")
                logger.info("断言通过！")
            except Exception as error:
                logger.error("断言失败！")
                raise error
        elif k.startswith("$"):
            # k是jsonpath表示式，用于从响应结果提取数据的  ； v是预期结果
            ac_result = jsonpath(result.json(), k)[0]
            try:
                assert ac_result == v
                logger.info(f"用例执行结果：{ac_result}")
                logger.info(f"用例预期结果：{v}")
                logger.info("断言通过！")
            except Exception as error:
                logger.error("断言失败！")
                raise error
