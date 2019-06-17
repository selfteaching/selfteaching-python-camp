from mymodule import stats_word
import os
import json
count = 20
dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname,'tang300.json')
with open(file_path,'r',encoding = 'UTF-8') as a:
    text = a.read()

print(stats_word.stats_text_cn(text,20))


 
 



