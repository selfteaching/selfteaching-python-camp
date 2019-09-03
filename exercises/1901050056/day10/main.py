from mymodule import stats_word
import json

with open('tang300.json',mode='r+',encoding='utf-8') as t:
   t1=t.read()
try:
    print(stats_word.stats_text(t1,20))
except  ValueError as va:
    print(va)
