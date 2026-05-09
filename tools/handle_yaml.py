'''
读取yaml文件数据，并返回内容
'''
import yaml


def read_yaml(yamlfile):
    with open(yamlfile, encoding="utf8") as f:
        # Loader(加载模式):yaml.FullLoader(全部加载一般都用这个)
        content = yaml.load(f, Loader=yaml.FullLoader)
        return content

if __name__ == "__main__":
    from tools.handle_path import yaml_path

    print(read_yaml(yaml_path / "login_data.yml"))