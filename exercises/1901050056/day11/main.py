from mymodule import stats_word
import json

#with open('tang300.json',mode='r+',encoding='utf-8') as t:
   #t1=t.read()
try:
    word = stats_word.stats_text(stats_word.test_get_link(),100)
    stats_word.email(word)

except  ValueError as va:
    print(va)