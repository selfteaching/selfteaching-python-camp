
from mymodule import stats_word
from os import path
import traceback
import json
import re
import logging

logging.basicConfig(
    format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)

def load_file():
    # 获取文件路径
    file_path = path.join(path.dirname(path.abspath(__file__)),'tang300.json')
    print('当前路径：',__file__,'\n读取文件路径:',file_path)
    with open(file_path, 'r', encoding = 'utf-8')  as f :
        return f.read()

def merge_poems(data):
    poems = ''
    for item in data:
        poems += item.get('contents','')
    return poems

def main():
    try:
        data = load_file()
        logging.info(data[0])
        #logging.info(json.loads(data))
        poems = merge_poems(json.loads(data))
        logging.info('result ==> %s',stats_word.stats_text_cn(poems,100))
    except Exception as e:
        logging.exception(e)


if __name__ == "__main__":
    main()

'''
练习感受：

1）设置log方法
logging.basicConfig()。期中输出格式控制  %(filename)s  第一次遇到，值得注意。
使用时调用：logging.info()即可

2）获取当前路径方法
path.dirname(path.abspath(__file__))

3）打开文件方法
with open(file_path, 'r', encoding = 'utf-8')  as f

4）读取json格式数据方法
json.loads(data)   返回的是字典

'''