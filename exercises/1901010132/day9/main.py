from mymodule import stats_word
import json

with open(r'\Users\Administrator\Documents\GitHub\selfteaching-python-camp\exercises\1901010132\day9\tang300.json',encoding='UTF-8') as f:
    text=f.read()


stats_word.stats_text_cn(text, 100)