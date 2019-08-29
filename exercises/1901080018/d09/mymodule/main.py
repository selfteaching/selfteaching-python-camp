import stats_word
import json
import re
from os import path
file_path = path.join(path.dirname(path.abspath(__file__)),"tang300.json")
print(__file__,file_path)
with open(file_path,'r',encoding='utf-8') as f:
    str1 = f.read()
    r = json.loads(str1)
    j = ''
    for i in r:
        j = j + i.get('contents','')
    print(stats_word.stats_text_cn(j,100))