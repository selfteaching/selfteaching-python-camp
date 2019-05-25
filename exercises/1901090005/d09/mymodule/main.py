
import stats_word
import os
import json
count = 100
dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname,'tang300.json')
with open(file_path,'r', encoding='utf-8') as a:
    text = a.read()
try:
    new =stats_word.stats_text(text,count)
except Exception as e:
    print(e)

print(stats_word.stats_text_cn(text,count))


