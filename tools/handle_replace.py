import json
import re
from loguru import logger
from data.envi_data import EnviData
from tools.handle_gendata import HandleGendata

# getdata = HandleGendata()


# 后置处理替换字符串信息
def replace_mark(str_data):
    '''
    :param str_data: 需要替换数据的字符串
    :return: 返回替换后的字符串
    '''
    #  用正则匹配需要替换的字符串
    if str_data is None:
        logger.info("------没有读取要做替换字符串-------")
        return
    logger.info(f"原字符串：{str_data}")
    # 因为替换方法我们用了正则：只能查找字符串类型 传过来yaml结果直接是一个字典类型 ==序列化转化为字符串
    if type(str_data) != str:
        str_data = json.dumps(str_data)
    result = re.findall('\${(.*?)}', str_data)
    logger.info(f"需要替换的字符串：{result}")
    if result:
        logger.info(f"开始进行替换字符串:{result}")
        for mark in result:
            if mark.endswith("()"):
                logger.info(f"当前的值：{mark}")
                key = mark.strip('()') # 默认去掉字符串的前后空格，也可以指定删除的字符串
                # value = getattr(getdata, key)()
                value = eval(f"HandleGendata().{mark}")
                # 1. 替换字符串
                str_data = str_data.replace(f"${{{mark}}}", str(value))
                # 2. 存入环境变量
                setattr(EnviData, key, value)
            elif hasattr(EnviData, mark):
                value = getattr(EnviData, mark)
                str_data = str_data.replace(f"${{{mark}}}", str(value))
        logger.info(f"最终得到的字符串：{str_data}")
    return str_data
