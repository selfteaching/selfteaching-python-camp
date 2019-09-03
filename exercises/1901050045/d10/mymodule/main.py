import stats_word
import json
import jieba
with open('I:/Github/selfteaching-python-camp/exercises/1901050045/d09/mymodule/tang300.json',encoding='UTF-8') as f:
    text=f.read()
f.closed
    
try:
    stats_word.stats_text(text)
except ValueError:
    
    print ('参数格式错误或参数不存在,请重新输入字符串')

