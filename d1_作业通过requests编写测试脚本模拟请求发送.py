# 引入requests包
import requests
# 可像js那样调用
from types import SimpleNamespace
# 随机函数
import random
# 引入jsonpath处理数据
from jsonpath import jsonpath

# 登录请求
login_req = SimpleNamespace(**{
    "url": "http://shop.lemonban.com:8107/login",
    "method": "post",
    "header": {
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Language": "zh"
    },
    "params": {"principal": "13560088365", "credentials": "123456", "appType": 3, "loginType": 0}
})
resp_login = requests.request(login_req.method, login_req.url, headers=login_req.header,
                              json=login_req.params)

resp_login_obj = SimpleNamespace(**resp_login.json())
token = resp_login_obj.token_type + resp_login_obj.access_token
print(token)

# 商品搜索
search_req = SimpleNamespace(**{
    "url": "http://shop.lemonban.com:8107/search/searchProdPage",
    "method": "get",
    "header": {
        "Accept-Language": "zh"
    },
    "params": {"prodName": "真皮圆筒包"}
})

resp_search = requests.request(search_req.method, search_req.url, headers=search_req.header,
                               params=search_req.params)

resp_search_list = resp_search.json()["records"]

# 在返回的列表中随机获取一个进入查看详情及后面添加购物车的操作
num = random.randint(0, len(resp_search_list) - 1)
# 获取产品id
prodId = resp_search_list[num]["prodId"]

# 查看商品详情
prod_info_req = SimpleNamespace(**{
    "url": "http://shop.lemonban.com:8107/prod/prodInfo",
    "method": "get",
    "header": {
        "Accept-Language": "zh"
    },
    "params": {"prodId": prodId}
})
resp_prod_info = requests.request(prod_info_req.method, prod_info_req.url, headers=prod_info_req.header,
                                  params=prod_info_req.params)

resp_prod_info_obj = SimpleNamespace(**resp_prod_info.json())
# 获取shopId, skuId
shopId, skuId = resp_prod_info_obj.shopId, resp_prod_info_obj.skuList[0]["skuId"]
print(shopId, skuId)

# 将商品加入购物车
add_cart_req = SimpleNamespace(**{
    "url": "http://shop.lemonban.com:8107/p/shopCart/changeItem",
    "method": "post",
    "header": {
        "Authorization": token,
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Language": "zh"
    },
    "params": {"basketId": 0, "count": 1, "prodId": prodId, "shopId": shopId, "skuId": skuId}
})
resp_add_cart = requests.request(add_cart_req.method, add_cart_req.url, headers=add_cart_req.header,
                                 json=add_cart_req.params)
print(resp_add_cart.text)

# 获取购物车商品
get_cart_req = SimpleNamespace(**{
    "url": "http://shop.lemonban.com:8107/p/shopCart/info",
    "method": "post",
    "header": {
        "Authorization": token,
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Language": "zh"
    },
    "params": []
})
resp_get_cart = requests.request(get_cart_req.method, get_cart_req.url, headers=get_cart_req.header,
                                 json=get_cart_req.params)
# print(resp_get_cart.text)

# shopCartItems = resp_get_cart.json()[0]["shopCartItemDiscounts"][0]["shopCartItems"]
basketIds = jsonpath(resp_get_cart.json(), "$..basketId")
# print(basketIds)
# basketIds = [item["basketId"] for item in shopCartItems]
print(f"basketIds:{basketIds}")
# 结算商品
confirm_req = SimpleNamespace(**{
    "url": "http://shop.lemonban.com:8107/p/order/confirm",
    "method": "post",
    "header": {
        "Authorization": token,
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Language": "zh"
    },
    "params": {"addrId": 0, "basketIds": basketIds, "couponIds": [], "isScorePay": 0, "userChangeCoupon": 0,
               "userUseScore": 0, "uuid": None
               }
})
resp_confirm = requests.request(confirm_req.method, confirm_req.url, headers=confirm_req.header,
                                json=confirm_req.params)
print(resp_confirm.text)

# 提交订单
submit_req = SimpleNamespace(**{
    "url": "http://shop.lemonban.com:8107/p/order/submit",
    "method": "post",
    "header": {
        "Authorization": token,
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Language": "zh"
    },
    "params": {"orderShopParam": [{"remarks": "", "shopId": shopId}], "uuid": None}
})

resp_submit = requests.request(submit_req.method, submit_req.url, headers=submit_req.header,
                               json=submit_req.params)
print(resp_submit.text)
