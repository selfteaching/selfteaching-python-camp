import json
import stats_word

with open('/Users/mac/Documents/GitHub/selfteaching-python-camp//exercises/1901050017/d09/mymodule/tang300.json','r',) as s:
    t = s.read()
try : 
    print(stats_word.stats_text_cn(t,100))
except ValueError as error :
    print(error)
