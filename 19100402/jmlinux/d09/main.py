import json
from mymodule import stats_word
text1 = {}

with open('tang300.json',encoding='utf-8') as f:
    text = f.read()

try:
    print("词频最高的前100个词",stats_word.stats_text_cn(text,100))
    pass
except ValueError as ve :
    print(ve)