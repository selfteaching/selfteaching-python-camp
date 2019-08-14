from mymodule import stats_word
import json
import os
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json'),encoding='UTF-8') as f: 
    data = f.read()   
try:
    print(stats_word.stats_text_cn(data))
except Exception as e:
    print('erro=>',e)