from collections import Counter
from stats_word import stats_text_cn
import json

with open('tang300.json','r',encoding='UTF-8') as f:
     read_data = f.read()
f.closed
print(read_data)
   
try:
    print(stats_word.stats_text_cn(read_data))
except NameError as err:                    
    print('Oops, cannot find text! Please input text!')