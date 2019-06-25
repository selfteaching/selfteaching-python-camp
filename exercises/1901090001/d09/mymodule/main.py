import stats_word
import json
count = 100
with open('tang300.json','r',encoding='utf-8') as file:
    text = file.read()
print(stats_word.stats_text_cn(text))

try:
    stats_word.stats_text_cn(text)
except ValueError:
    print('Invalid string')
