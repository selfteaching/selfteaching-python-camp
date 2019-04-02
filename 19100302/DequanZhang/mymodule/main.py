import os
import json

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json'))  as f:
    read_data = f.read()

from stats_word import stats_text_cn 

print('词频统计Top20',stats_text_cn(read_data,20))
