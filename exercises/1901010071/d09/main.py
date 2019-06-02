import stats_word
import json
with open('tang300.json','r', encoding='UTF-8') as f: #不加'r', encoding='UTF-8'会报UnicodeDecodeError
    read_date = f.read()
f.closed

try:
    print('统计字数最多的前100个字： \n',stats_word.stats_text_cn(read_date,100))
except ValueError as w:
    print(w)        

