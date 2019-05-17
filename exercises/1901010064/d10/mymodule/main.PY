import stats_word
import json
import os
import re

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json')


with open(file_path, 'r', encoding='utf-8') as f:
    f1=f.read()#f1为str
    f2=stats_word.stats_text_cn(f1,20)
    print(f2)

