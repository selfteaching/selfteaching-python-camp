
import os
from collections import Counter

file_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'tang300.json')
print(file_path)
with open(file_path,'r',encoding='utf-8') as f:
    a=f.read()
import stats_word
print(stats_word.stats_text_cn(a,100))




