
from mymodule import stats_word
import json
try:
    with open('tang300.json','r', encoding='UTF-8')as i:
        txt=i.read()
    print(stats_word.stats_txt_cn(txt))
except ValueError as r:
    print(r)