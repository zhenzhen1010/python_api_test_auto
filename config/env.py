# 引入第三方库
import yaml
from pathlib import Path


class Config:
    _instance = None
    env = "test"  # 默认测试环境
    data = {}  # 数据为空

    # 从写类实例函数，实现单例模式
    def __new__(cls):
        # 判断是否创建类实例
        if not cls._instance:
            # 类实例没有被创建时，创建类
            cls._instance = super().__new__(cls)
        # 如果已存在，返回已创建的类实例
        return cls._instance

    # 加载配置文件
    def load(self, env_name):
        self.env = env_name
        # 配置文件地址
        path = Path(__file__).parent / f"{env_name}.yaml"
        # 读取文件
        with open(path, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

config = Config()