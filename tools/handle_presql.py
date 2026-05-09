# json字符串反序列化和序列化方法
import json
# sql查询封装方法
import allure

from tools.handle_mysql import HandleMysql
# 日志信息
from loguru import logger
# 数据库配置信息
from data.setting import mysql_config
# 环境变量
from data.envi_data import EnviData
from tools.handle_replace import replace_mark


# 封装前置处理sql的方法
@allure.step("前置SQL处理")
def pre_sql_fun(sql_data):
    # 判空处理
    if sql_data is None:
        logger.info("sql_data为空，不需要处理")
        return
    # 反序列化
    if type(sql_data) == str:
        sql_data = json.loads(sql_data)
    # 实例化数据库对象
    handle_mysql = HandleMysql(**mysql_config)
    # 循环获取里面的k，v
    for k, v in sql_data.items():
        # 替换字符串
        v = replace_mark(v)
        logger.info(f"替换后的值是：{v}")
        # 读取数据库，获取对应的字段值
        result = handle_mysql.select_sql(v)
        logger.info(f"key值是：{k}")
        logger.info(f"value值是：{result}")
        # 设置key和value到环境变量中，供后续调用
        setattr(EnviData, k, result[k])
    print(EnviData.__dict__)

if __name__ == "__main__":
    sql = '''{"mobile_code":"select mobile_code  from tz_sms_log where user_phone='13560088360' order by rec_date desc limit 1;"}'''
    pre_sql_fun(sql)
