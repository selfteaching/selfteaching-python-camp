# Filename : main.py
# author by : 张金磊

#import pandas as pd
from mymodule import stats_word

with open('./tang300.json', encoding='utf-8') as f: 
    tang_text = f.read()


try:
    stats_word.stats_text_cn(tang_text, 20)
except Exception as err:
    print(err)
    

        

 

