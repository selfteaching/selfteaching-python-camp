import stats_word
import json

with open('C:/Users/Charles/Documents/GitHub/selfteaching-python-camp/exercises/1901050059/d09/mymodule/tang300.json','r',encoding='UTF-8') as f:
    text = f.read()
f.closed

try:
    print(stats_word.stast_text_cn(text,100))
except ValueError as w:
    print(w)
