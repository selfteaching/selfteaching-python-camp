import stats_word
import json
with open('C:/Users/13501/Documents/GitHub/selfteaching-python-camp/exercises/1901050028/d09/mymodule/tang300.json',encoding='UTF-8') as f:   
    text=f.read()

try:
    print(stats_word.stats_text_cn(text,20))
finally:
    if f:
        f.close()
