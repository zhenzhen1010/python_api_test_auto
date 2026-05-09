'''
文件路径处理 --- 日志文件、excle文件、图片文件 等等 ===统一放在公共管理 ---公共方法/功能层tools目录下的py模块来管理
'''
# 引入文件路径包
import pathlib

# 日志文件的路径处理
log_path = pathlib.Path(__file__).parent.parent/"logs"/"mall_api.log"
# 测试用例excel文件的路径处理
excel_path = pathlib.Path(__file__).parent.parent/"data"/"testcase_mall.xlsx"
# 图片测试数据文件路径的处理
pic_path = pathlib.Path(__file__).parent.parent/"data"/"code.jpeg"
# 报告路径
report_path = pathlib.Path(__file__).parent.parent/"allure_reports"
# 公钥路径
public_key_path = pathlib.Path(__file__).parent.parent/"data"/"rsa_public_key.pem"
# 前程贷测试用例
qcd_path = pathlib.Path(__file__).parent.parent/"data"/"testcase_qcd.xlsx"
# yaml用例路径
yaml_path = pathlib.Path(__file__).parent.parent/"data"/"yaml"


# 调试状态下执行
if __name__ == '__main__':
    print(log_path)
    print(excel_path)
