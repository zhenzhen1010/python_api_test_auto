# 引入base64库
import base64
# 引入RSA加密库，公密钥
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def encrypt_with_rsa(data, public_key_path):
    # 转换成二进制
    data_bytes = data.encode("UTF8")

    with open(public_key_path) as file:
        public_key_str = file.read()
    # 通过RSA导入公钥信息，并返回公钥对象
    public_key = RSA.importKey(public_key_str)
    # 基于公钥对象创建RSA加密器对象
    pk = PKCS1_v1_5.new(public_key)
    # 通过加密器对象进行加密
    data_rsa = pk.encrypt(data_bytes)  # 返回二进制数据
    # 需进行base64转码才能转化为字符串文本
    data_base64 = base64.b64encode(data_rsa)
    # 将二进制文件转成文本
    return data_base64.decode('utf8')
