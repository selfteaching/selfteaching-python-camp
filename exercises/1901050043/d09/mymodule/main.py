import json
import stats_word

with open('C:/Users/apple/Documents/GitHub/selfteaching-python-camp/exercises/1901050043/d09/mymodule/tang300.json','r',encoding='UTF-8') as f:
    t=f.read()
try:
    print(stats_word.stats_text_cn(100,t),'\n')
except ValueError as error:
    print(error)





