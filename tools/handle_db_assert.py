"""
数据库断言思路：
第一步：因为有变量的调用  先完成变量的替换
   - 我现在没有在用例去跑  也就是没有执行前面接口 如果直接去替换 环境变量里是没有这个orderNumbers这个属性的
   - 如果要调试的话 需要再replace方法里假设一个环境变量的属性
第二步：反序列化转化成字典
第三步： for循环遍历得到key和value
   - k： sql语句 用于去数据库里进行数据的查询操作 得到查询结果 --执行结果
   - v： 预期结果 用于个执行结果做断言
第四步： 用k去查询数据库了
   -数据库的结果是字典：{'count(1)': 1}  {'status': 2}  真正用于去做断言的是value

封装函数的步骤：
第一步： 功能代码写出来 --done
第二步： def封装
第三步： 参数化： 如果有一些变化的数据/不确定的数据 设置为形参
第四步： 设置返回值： 这个函数是否有数据要给调动的人使用；就是替换完成后的字符串 --断言不需要返回值

一个函数封装完了 ，函数优化：
1、判空： 有些数据没有这提取字段 读取出来结果None
  - 直接做反序列化的操作 就会报错： json格式错误
2、加上日志和异常捕获： 方便进行问题定位和排查: 但凡确实结果的位置都可以加上日志【print的地方】
  - 断言方法都要做异常捕获的

"""
import json

import allure

from tools.handle_replace import replace_mark
from tools.handle_mysql import HandleMysql
from data.setting import mysql_config
from loguru import logger

@allure.step("做数据库断言")
def db_assert_fun(db_data):
    if db_data is None:
        logger.info("====================这条用例不需要做数据库的断言===================")
        return
    logger.info("====================开始做数据库的断言！===================")
    db_data = replace_mark(db_data)
    db_data = json.loads(db_data)
    logger.info(f"数据库断言的表达式：{db_data}")
    for k,v in db_data.items():
        sql_result = HandleMysql(**mysql_config).select_sql(k) # 数据库的结果是字典：{'count(1)': 1}  {'status': 2}
        for i in sql_result.values(): #i 就是执行结果
            logger.info(f"数据库的实际查询结果：{i}")
            logger.info(f"数据库的预期结果：{v}")
            try:
                assert i == v
                logger.info("数据库断言通过！")
            except AssertionError as e:
                logger.error("数据库断言失败！")
                raise e

if __name__ == '__main__':
    # excel读取原始数据
    db_data = """{"select count(1) from tz_order where order_number = '#orderNumbers#'":1, 
    "select status from tz_order where order_number = '#orderNumbers#'":2}"""
    db_assert_fun(db_data)
