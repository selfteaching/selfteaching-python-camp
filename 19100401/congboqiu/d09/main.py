import re
from mymodule import stats_word
import json
with open(r'''C:\Users\win10\Documents\GitHub\selfteaching-python-camp\19100401\congboqiu\d09\tang300.json''','r+',encoding="utf-8") as f:
    text='f.read()'
print(stats_word.stats_text_cn(text,100))