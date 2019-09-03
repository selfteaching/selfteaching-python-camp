
import re
import stats_word
import json
import jieba

with open('/Users/apple/Documents/GitHub/selfteaching-python-camp/exercises/1901010053/d10/mymodule/tang300.json','r',encoding='UTF-8') as f:
    text=f.read()


stats_word.stats_text_cn(text, 20)