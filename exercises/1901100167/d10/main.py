import sys
import json
import os
import jieba
from collections import Counter
sys.path.append('e:\\self-teaching\\selfteaching-python-camp\\exercises\\1901100167\\d09')
file_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'tang300.json')
print(file_path)
with open(file_path,'r',encoding='utf-8') as f:
    a=f.read()
from mymodule import stats_word
try:
    print(stats_word.stats_text_cn(a))
except TypeError as e:
    print ("error:%s"%e)
