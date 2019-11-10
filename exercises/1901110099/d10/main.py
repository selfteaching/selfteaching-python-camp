from mymodule import stats_word
from os import path
import json
import re


file_path= path.join(path.dirname(path.abspath(__file__)), 'tang300.json')

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        poem= f.read()
        print(stats_word.stats_text_cn(poem, 20))

except TypeError as e:
    print ("error:%s"%e)



