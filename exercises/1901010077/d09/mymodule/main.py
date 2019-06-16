import stats_word
import json
with open('tang300.json','r', encoding='UTF-8') as f: #不加'r', encoding='UTF-8'会报UnicodeDecodeError
    t = f.read()
f.closed

try:
    print('词频最高的前100个词：')
    stats_word.stats_text_cn(t,100)
except ValueError as w:
    print(w)        