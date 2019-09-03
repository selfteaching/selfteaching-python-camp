

import stats_word
import json
with open('tang300.json','r', encoding='UTF-8') as f: 
    read_date = f.read()

try:
    print('前20的词频数： \n',stats_word.stats_text_cn(read_date,20))
except ValueError as w:
    print(w)        


