# 引入第三方库
from jsonpath import jsonpath
# 引入内置函数
import json

json_text = {"actualTotal": 999.0, "total": 1998.0, "totalCount": 2, "orderReduce": 999.0}

# actualTotal = parse('$.actualTotal').find(json_text)[0].value
actualTotal = jsonpath(json_text, "$..actualTotal")[0]
print(actualTotal)

# 反序列化-json字符串转换成python字典
json_str = '{"key":"value","enable":true}'
py_json = json.loads(json_str)
print(py_json, type(py_json))

# 序列表-python字典转json字符串
py_dict = {"key": "value", "enable": True}
json_dict = json.dumps(py_dict)
print(json_dict, type(json_dict))
