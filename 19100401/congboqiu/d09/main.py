import re
from mymodule import stats_word
import json


with open('tang300.json','r',encoding='UTF-8') as f:
    text=f.read()


stats_word.stats_text_cn(text, 100)
