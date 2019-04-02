from mymodule import stats_word_day9
import json


with open("tang300.json", "r", encoding='utf-8') as f:
    text_tang = f.read()

stats_word_day9.stats_text_cn(text_tang, 100)