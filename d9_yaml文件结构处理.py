'''
yaml文件处理测试用例：
    -后缀：.yml,yaml

'''
import yaml

with open("./data/yaml/login_data.yml",encoding="utf8") as f:
    # Loader(加载模式):yaml.FullLoader(全部加载一般都用这个)
    content = yaml.load(f,Loader=yaml.FullLoader)
    print(content,type(content))