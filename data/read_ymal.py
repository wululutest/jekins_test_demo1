
import yaml
from config import Base_Url


def build_data_func():  # 一. 自定义解析方法
    # 2.读取文件
    filename = Base_Url + '/data/search_data.yaml'
    with open(filename, 'r', encoding='utf-8') as file:
        # 3.调用方法获取数据
        data = yaml.safe_load(file)
        print(data)
        return data  # 二. 添加函数返回值
