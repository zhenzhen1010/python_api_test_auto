'''
数据库操作封装
    -日志 + 异常捕获
    -用户控制输入-容易出现异常的情况，--整个sql查询，加上异常描述
    -finally：不管是否正常都执行，关闭游标+连接
'''
# 引入工具库
from pymysql import connect, cursors
# 引入日志工具库
from loguru import logger


# 定义数据库操作类
class HandleMysql:

    # 实例初始化方法
    def __init__(self, host, port, database, user, password):
        # 数据库连接作为实例属性
        self.conn = connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
            charset="utf8mb4",
            cursorclass=cursors.DictCursor  # 使用字典形式返回数据
        )
        # 获取指针作为实例方法
        self.cur = self.conn.cursor()

    # 定义查询数据库方法
    def select_sql(self, sql: str, fetch=1, size=None):
        '''
        :param sql: 查询语句
        :param fetch: 返回条数：1-返回一条数据，2-返回多条数据，结合size传参，3-返回全部数据
        :param size: 默认返回1条
        :return: 返回1条数据时字典，多条时返回列表字典
        '''
        try:
            result = self.cur.execute(sql)
            logger.info(f"查询到的结果条数：{result}")
            # 第四步：获取数据（从游标位置开始）
            if result > 0:
                if fetch == 1:
                    data = self.cur.fetchone()
                    logger.info(f"查询到的结果：{data}")
                    return data
                elif fetch == 2:
                    data = self.cur.fetchmany(size=size)
                    logger.info(f"查询到的结果：{data}")
                    return data
                elif fetch == 3:
                    data = self.cur.fetchall()
                    logger.info(f"查询到的结果：{data}")
                    return data
                else:
                    # print("输入的值不在范围内！")
                    logger.error(f"输入的值不在范围内！输入的值：{fetch}")
            else:
                # print("无查询到符合条件的数据！")
                logger.info(f"无查询到符合条件的数据!{result}")
        except Exception as error:
            # print(f"查询数据异常！{error}")
            logger.error(f"查询数据异常！{error}")
        finally:
            self.cur.close()
            self.conn.close()


if __name__ == "__main__":
    from data.setting import mysql_config

    sql = "SELECT id,user_phone,mobile_code FROM tz_sms_log WHERE user_phone = '13560088365'"
    print(HandleMysql(**mysql_config).select_sql(sql, fetch=3))
