from stats_word import stats_text
import json
import os
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json'), encoding = 'UTF-8') as f:
    read_date = f.read()
f.closed
    
try:
    print(stats_text(read_date,20))
except TypeError:
    print('The input is not string...')
