import stats_word
import json
from os import path

with open(path.join(path.dirname(path.abspath(__file__)), 'tang300.json'),encoding='UTF-8') as f :
    text = f.read()

count=100

try:
    print(stats_word.stats_text_cn(text, count))
except ValueError as fnf_error:
        print(fnf_error)
