from openpyxl import load_workbook


# 函数封装
def read_excel(excel, sheet):
    '''
    desc: 这是读取excel单个表单所有数据的方法
    :param excel: 文件路径名
    :param sheet: 表单名
    :return: 整个表单的所有数据，保存为列表嵌套字典的格式
    '''
    # 读取文件 .xlsx
    wb = load_workbook(excel)
    # 读取表单
    sh = wb[sheet]
    # 定义空列表存放数据
    list_case = []
    # 取出表单所有数据，转换成字典格式存储
    cases = list(sh.values)
    # 取出标题
    heading = cases[0]
    # 依次读取每条数据
    for case in cases[1:]:
        # 组装转换成字典格式数据
        data = dict(zip(heading, case))
        # 将数据添加到存储列表中
        list_case.append(data)
    # 返回出去
    return list_case


if __name__ == "__main__":
    # 导入excel存放路径文件
    from tools.handle_path import excel_path

    print(read_excel(excel_path, "login"))
