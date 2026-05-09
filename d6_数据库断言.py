'''
思路：
    第一步：因为有变量的调用，先完成变量的替换
        -没跑用例，直接替换会报错，因为环境变量没用这个值
        -如果是调试，可以先预设一个值
    第二步：反序列化转化成字典
    第三步：for循环遍历的key和value
        -k：sql语句 用于去数据库进行查询操作

'''
from data.envi_data import EnviData
from tools.handle_replace import replace_mark
import json
from tools.handle_mysql import HandleMysql
from data.setting import mysql_config




def db_assert_fun(sql):
    # 替换字符串
    sql_assert = replace_mark(sql)
    # 转字典
    sql_assert = json.loads(sql_assert)

    # 遍历字典
    for sql, result in sql_assert.items():
        # 查询数据库
        ressql = HandleMysql(**mysql_config).select_sql(sql)
        try:
            assert list(ressql.values())[0] == result
        except Exception as error:
            print(error)

if __name__ == "__main__":
    setattr(EnviData, 'orderNumbers', '2049441623749955584')
    sql_assert = '''{"select count(1) from tz_order where order_number = '${orderNumbers}'":1, 
    "select status from tz_order where order_number = '${orderNumbers}'":2}'''
    db_assert_fun(sql_assert)