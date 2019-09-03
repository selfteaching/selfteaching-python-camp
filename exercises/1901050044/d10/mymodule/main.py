import json
import stats_word
import jieba
with open('/Users/maminyi/Documents/GitHub/selfteaching-python-camp/exercises/1901050044/d10/mymodule/tang300.json', encoding = 'UTF-8') as f:
    text = f.read()
print(stats_word.stats_text_cn(text,20))