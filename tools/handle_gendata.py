'''
利用第三方Fask库随机生成数据
'''
# 引入库
from faker import Faker
# 引入数据库查询方法
from tools.handle_mysql import HandleMysql
# 数据库配置信息
from data.setting import mysql_config
# 日志组件
from loguru import logger


class HandleGendata:

    def __init__(self):
        # 设置中国区
        self.fk = Faker(locale='zh_CN')
        # self.mysql = HandleMysql(**mysql_config)

    def gen_unregister_phone(self):
        while True:
            #   调用方法生成手机号码
            phone = self.fk.phone_number()
            #   查询数据库，是否存在这个手机号码
            sql = f'select * from tz_user where user_mobile ="{phone}"'
            result = HandleMysql(**mysql_config).select_sql(sql)
            if result:
                # 跳出本次循环，继续生成phone
                continue
            else:
                logger.info(f"生成的手机号码是：{phone}")
                # 结束循环 返回phone值
                return phone

    def gen_unregister_name(self):
        while True:
            # 调用方法生成用户名
            userName = self.fk.user_name()
            # 查询数据库，是否存在这个用户名
            sql = f'select * from tz_user where nick_name = "{userName}"'
            logger.info(f"sql语句：{sql}")
            result = HandleMysql(**mysql_config).select_sql(sql)
            if result or (len(userName) > 16 or len(userName) < 4):  # 非空 或者 长度不符合要求 都要重新生成用户名
                # 跳出本次循环，继续生成userName
                continue
            else:
                logger.info(f"生成的用户名是：{userName}")
                # 结束循环 返回userName值
                return userName
            return userName


if __name__ == "__main__":
    handle_gendata = HandleGendata()
    print(handle_gendata.gen_unregister_uname())
