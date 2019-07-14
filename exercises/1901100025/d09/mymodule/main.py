import os
import json
import stats_word
with open('/Users/zhiyutian/Documents/New/selfteaching-python-camp/exercises/1901100025/d09/mymodule/tang300.json', 'r', encoding = 'utf-8') as f:
    text_tang = json.load(f)
    c = []
    for d in text_tang:
        for key in d:
            c.append(str(d[key]))
    c = str(c)
print(stats_word.stats_text_cn(c))