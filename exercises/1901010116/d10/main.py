from mymodule import stats_word
from os import path

file_path = path.join(path.dirname(path.abspath(__file__)), './tang300.json') #获取同一文件夹下文件路径
with open(file_path, 'r', encoding='utf-8') as f: #打开tang300.json 
    #用try...except捕获异常
    try:
        print('文件中汉字词频最高的前20个词：\n',stats_word.stats_text_cn(f.read(),20))
    except ValueError:
        print('ValueError: Oops! That was no valid string.')