from stats_word import *
from os import path

file_path = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')
print('当前文件路径： ', __file__, '\n读取文件路径： ', file_path)

with open(file_path, 'r', encoding = 'utf-8') as f:
    a = []
    a = f.read()
    try : 
        print('100中文词频统计结果：', stats_text_text(a,100))
    except ValueError as ve:
        print(ve) 