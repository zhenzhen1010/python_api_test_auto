'''
图形验证码识别
    1、开发设置绕过/万能验证码（常用）
    2、使用第三方工具库（没用办法时使用）
        ddddocr：简单验证码能识别，复杂的做不了
        图鉴（收费网站）：
'''
import uuid
import ddddocr
import requests

# 1）拿到要处理的验证码图片： 调用获取验证码图片的接口
url = "http://shop.lemonban.com:8108/captcha.jpg"
# 生成一个uuid值： 调用验证码接口用 + 登录接口 用的是同一个uuid的值
uuid_value = str(uuid.uuid4())
param = {"uuid":uuid_value}
res = requests.request("get",url,params=param)
# 这个响应就是图片本身
print(res.content)  # 二进制字节 图片数据

# 2）调用处理验证码的接口【第三方接口 库】，获取验证码的内容。-图片文本内容
ocr = ddddocr.DdddOcr()
result = ocr.classification(res.content) # 直接传入图片二进制数据进行处理，不需要图片的文本内容
print(result)

# 3) 登录接口，验证码传输值。
login_url = "http://shop.lemonban.com:8108/adminLogin"
login_param = {
        "principal":"student",
        "credentials":"lemon!@666",
         "sessionUUID":uuid_value,
        "imageCode":result
}
login_res = requests.request("post",login_url,json=login_param)
print(login_res.text)