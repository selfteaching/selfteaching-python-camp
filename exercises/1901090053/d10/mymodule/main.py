
import stats_word as sw 
import json

with open('tang300.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data = str(data)
sw.stats_text_cn(data,100)