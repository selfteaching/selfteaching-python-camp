from mymodule import stats_word
import json
with open('tang300.json','r',encoding='UTF-8') as f:
    text = f.read()
f.close
try:
    stats_word.stats_text_cn(text,100)
except ValueError:
    print('Error: input is not string.')

