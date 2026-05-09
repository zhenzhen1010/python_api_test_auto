"""
封装这个方法得到时间戳 以及sign数据  存储到环境变量里
  - excel调用这个变量  完成替换操作

因为一个项目的加密算法和规则统一的。针对这个项目可以封装这个方法使用
"""
import time
from data.envi_data import EnviData
from tools.handle_rsa_encry import encrypt_with_rsa
from tools.handle_path import public_key_path
from loguru import logger


def encryto_sign():
    # 准备时间戳
    timestamp = int(time.time())
    # 加上一个判断 是否有token属性
    if hasattr(EnviData, "token"):
        # 取到token值
        token = getattr(EnviData, "token")
        # token的前50位
        sub_token = token[0:50]
        # 跟时间戳进行拼接
        data = sub_token + str(timestamp)
        # RSA加密
        sign = encrypt_with_rsa(data, public_key_path)
        setattr(EnviData, "timestamp", timestamp)
        setattr(EnviData, "sign", sign)
        logger.info(f"环境变量的数据是：{EnviData.__dict__}")
