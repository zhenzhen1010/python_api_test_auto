# 导入包
import requests
from tools.handle_requests_bak import Requests

# 准备请求的四大要素
# url = "http://shop.lemonban.com:8107/search/searchProdPage"
# method = "GET"
# param = {"prodName": "圆筒包"}
# header = {"Accept-Language": "zh"}
# res = requests.request(method, url, headers=header, params=param)
# print(res.text)

# 发送 post 请求
# post_url = "http://shop.lemonban.com:8107/login"
# post_method = "POST"
# post_param = {"principal": "13560088365", "credentials": "123456", "appType": 3, "loginType": 0}
# header = {"Accept-Language": "zh"}
#
# post_res = requests.request(post_method, post_url, headers=header, json=post_param)
# print(post_res.json())
# login_token = post_res.json()["access_token"]

# post form-data 格式
# post_form_data_url = "http://erp.lemonban.com/user/login"
# post_form_data_param = {"loginame":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
# post_form_data_method = "post"
# header = {"Accept-Language": "zh"}
# post_form_data_res = requests.request(post_form_data_method, post_form_data_url, headers=header, data=post_form_data_param)
# print(post_form_data_res.json())
# 上传文件

# file_req_url = "http://shop.lemonban.com:8107/p/file/upload"
# method = "post"
# file_obj = {"file": (open("code.jpeg", "rb"))}
# header = {"Accept-Language": "zh", "Content-Type": "multipart/form-data",
#           "Authorization": "bearer" + login_token}  # 调用token的值
# 一定要去掉content-type 不然会报错
# header.pop("Content-Type")
# resp = requests.request(method, file_req_url, files=file_obj, headers=header)
# print(resp.text)


#session鉴权的请求
# 初始化session对象，后面的接口请求都用session
# session = requests.Session()

# # 先登录接口--ERP
# url = "http://erp.lemonban.com/user/login"
# meth = "POST"
# param = {"loginame":"test1","password":"e10adc3949ba59abbe56e057f20f883e"}
# resp = session.request(method=meth,url=url,data=param)
# print(resp.json())  # 把json格式的响应数据，转换成python字典
# print("http响应头中的cookies：",dict(resp.cookies)) # 获取cookie
#
# # 做登录之后的添加接口
# url = "http://erp.lemonban.com/supplier/add"
# meth="post"
# param = {"info":'{"supplier":"1213","contacts":"","telephone":"","email":"","phonenum":"","fax":"","BeginNeedGet":"","BeginNeedPay":"","AllNeedGet":"","AllNeedPay":"","taxNum":"","taxRate":"","bankName":"","accountNumber":"","address":"","description":"","type":"客户","enabled":1}'}
# resp = session.request(method=meth,url=url,data=param)
# print(resp.json())  # 把json格式的响应数据，转换成python字典
# print("http响应头中的cookies：",dict(resp.cookies)) # 获取cookie

myRequests = Requests()
# 测试get方法
# url = "http://shop.lemonban.com:8107/search/searchProdPage"
# method = "GET"
# param = {"prodName": "圆筒包"}
# header = {"Accept-Language": "zh"}
#
# res = myRequests.get(url, header=header, param=param)
# print(res.text)
#
# # 测试post方法
# url = "http://shop.lemonban.com:8107/login"
# post_method = "POST"
# param = {"principal": "13560088365", "credentials": "123456", "appType": 3, "loginType": 0}
# header = {"Accept-Language": "zh"}
# res = myRequests.post(url, header=header, param=param)
# login_token = res.json()["access_token"]
# print(res.text)
#
# # 上传文件
#
# url = "http://shop.lemonban.com:8107/p/file/upload"
# method = "post"
# file_obj = {"file": (open("code.jpeg", "rb"))}
# header = {"Accept-Language": "zh", "Content-Type": "multipart/form-data",
#           "Authorization": "bearer" + login_token}  # 调用token的值
# res_file = myRequests.post(url, header=header, param=file_obj)
# print(res_file.text)

# post form-data 格式
# url = "http://erp.lemonban.com/user/login"
# param = {"loginame":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
# header = {"Accept-Language": "zh", "Content-Type":"application/x-www-form-urlencoded"}
# res_form_data = myRequests.post(url, header=header, param=param)
# print(res_form_data.text)
