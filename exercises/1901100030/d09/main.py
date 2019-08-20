# day9 标准库使用
# 2019年7月16日
# 陈浩 学号 1901100030

from mymodule import stats_word
import traceback
import logging
from os import path
import re
import json

logging.basicConfig(format="file:%(filename)s|line:%(lineno)d|message:%(message)s",level=logging.DEBUG)

def load_file():
    file_path = path.join(path.dirname(path.abspath(__file__)), "tang300.json")
    print("当前文件路径:", __file__,"\n读取文件路径：", file_path)
    
    with open(file_path,"r", encoding="utf-8") as f:
        return f.read()

def merge_poems(data):
    poems = ""
    for item in data:
        poems += item.get("contents","")
    return poems

def main():
    try:
        data = load_file()
        # print(data)
        logging.info(data[0])
        poems = merge_poems(json.loads(data))
        #print(poems)
        logging.info("result => %s", stats_word.stats_text_cn(poems,100))
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    main()



