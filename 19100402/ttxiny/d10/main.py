from mymodule import stats_word
import json
import jieba
with open('./tang300.json','r') as f:
    text = f.read()
try:
    stats_word.stats_text_cn(text,20)
except ValueError:
    print('Error: input is not string.')

