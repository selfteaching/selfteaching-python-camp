from mymodule import stats_word
import json
count = 20
with open('tang300.json','r',encoding='utf-8') as file:
    text = file.read()
    print(stats_word.stats_text_cn(text,count))

# try:
#     stats_word.stats_text_cn(text,count)
# except ValueError:
#     print('Invalid string')
