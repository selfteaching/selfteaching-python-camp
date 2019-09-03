import stats_word
import json
path = r'E:\python410\d10\mymodule\tang300.json'
with open(path,'r', encoding='UTF-8') as f: 
    t = f.read()

try:
    print('词频最高的前20个词：\n',stats_word.stats_text_cn(t,20))
except ValueError as w:
    print(w)        