'''
接口信息：
1、发送手机验证码
    - put http://shop.lemonban.com:8107/user/sendRegisterSms
    - {"mobile":"13560088360"}
第二步执行前：需要查询数据库，获取验证码
调用前面封装的sql方法
2、检验验证码
    - put http://shop.lemonban.com:8107/user/checkRegisterSms
    -{"mobile":"13560088360","validCode":"902660"}
3、注册用户
    - put http://shop.lemonban.com:8107/user/registerOrBindUser
    {"appType":3,"checkRegisterSmsFlag":"b8898c4f512a4f66becbdadc3f3c7047","mobile":"13560088360","userName":"13560088360","password":"123456","registerOrBind":1,"validateType":1}
思路：


'''

# 读取sql字符串
presql_data = '{}'
