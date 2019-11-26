import os
import json
import stats_word

with open(r'G:\GitHub\selfteaching-python-camp\exercises\1901010112\d10\mymodule\tang300.json', 'r',encoding = 'utf-8') as f:
    text_tang = json.load(f)
    c = []
    for d in text_tang:
        for key in d:
            c.append(str(d[key]))
    c = str(c)
print(stats_word.stats_text_cn(c))



