# this is d10 exercise for using the third lib
# date: 2019.09.28
# author by: rtgong

import stats_word
from os import path
import json
import re
import logging

logging.basicConfig(
    format='file:%(filename)s|line:%(lineno)s|message:%(message)s',level=logging.DEBUG)

def load_file():#定义文件路径
    file_path = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')
    print('当前文件路径',__file__,'\n读取文件路径：',file_path)
    
    with open(file_path,'r',encoding='UTF-8') as f:
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
        poems = merge_poems(json.loads(data))
        print('前20汉字字频结果：',stats_word.stats_text_cn(poems,20))
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    main()
