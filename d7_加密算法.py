'''
1.MD5、SHA：简单加密，不可逆，长度固定，容易被破解。主要为了校验数据在传输过程中是否被修改，应用场景：密码加密、文件校验【哈希算法】
2.base64编码：进行编码前需要转二进制数据（.encode()）,不能算是加密算法，只能说是编码方式。【在项目中结合加密算法一起使用】
3.加密算法：AES、DES、RSA都需要密钥
    -AES、DES：属于对称加密算法，使用相同的密钥进行加密和解密，安全性低，密码容易泄露，但速度快
    -RSA：非对称加密算法，两个密钥，公钥【加密】和私钥【解密】，公钥可以给任何人使用，私钥只能被数据持有者使用【服务器】
4.python提供丰富的加密库，base64、hashlib、crypto
'''

# 引入MD5加密库
import hashlib
import requests
# 引入base64库
import base64
# 引入RSA加密库，公密钥
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

# MD5加密
data = '123456'
# 先转化为二进制数
data_bytes = data.encode('utf8')
# 使用md5进行加密
data_md5 = hashlib.md5(data_bytes).hexdigest()  # e10adc3949ba59abbe56e057f20f883e
print(data_md5)

passwd = "123456"
# 转化二进制
passwd_bytes = passwd.encode("utf8")
# 加密成md5
passwd_md5 = hashlib.md5(passwd_bytes).hexdigest()

url = "http://erp.lemonban.com/user/login"
method = "POST"
param = {"loginame": "test1", "password": passwd_md5}

res = requests.request(method, url, params=param)
print(res.text)

# 对图片进行base64转码
# 第⼀步：open⽅法打开图⽚，得到⼆进制数据
with open('code.jpeg', 'rb') as f:
    # 得到二进制文件，不需要再进行二进制转换
    pic_data = f.read()  # 得到就是二进制数据
    # 对二进制数据进行base64转换
    pic_base64 = base64.b64encode(pic_data)
    # 把二进制数据转化成字符串
    pic_bt_str = pic_base64.decode("utf8")

    print(type(pic_bt_str))

# RSA加密算法 【非对称】
data = "12345"  # 待加密的数据
data_bytes = data.encode("UTF8")  # 转化为⼆进制数据

# 读取公钥信息
with open("./data/rsa_public_key.pem") as file:
    public_key_str = file.read()
    # 通过RSA导入公钥信息，并返回公钥对象
    public_key = RSA.importKey(public_key_str)
    # 基于公钥对象创建RSA加密器对象
    pk = PKCS1_v1_5.new(public_key)
    # 通过加密器对象进行加密
    data_rsa = pk.encrypt(data_bytes) # 返回二进制数据
    # 需进行base64转码才能转化为字符串文本
    data_base64 = base64.b64encode(data_rsa)
    # 将二进制文件转成文本
    print(data_base64.decode('utf8'))
