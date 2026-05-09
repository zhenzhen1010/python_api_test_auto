import pytest
from loguru import logger

from tools.handle_path import report_path, log_path

# 生成日志--持久化存储
logger.add(sink=log_path,  # 调用路径处理的变量
           encoding="utf8",
           level="INFO",
           rotation="1 day",
           retention=20
           )
# 生成测试报告 --clean-alluredir 清除文件
pytest.main(["-sv", f"--alluredir={report_path}", "--clean-alluredir", "-m p0", "--env=test"])
# 查看页面测试报告  allure serve .\allure_reports\
