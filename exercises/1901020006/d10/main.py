from mymodule import stats_word

import json

from os import path

file_path = path.join(path.dirname(path.abspath(__file__)),'tang300.json')
with open(file_path,'r',encoding='utf-8') as f:
    text = f.read()
    print(stats_word.stats_text_cn(text, 100)) 


try:
    text
except ValueError:
    print("error:文本为非字符串")   

