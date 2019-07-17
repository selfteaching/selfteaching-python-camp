from mymodule import stats_word
import json

with open(r'C:\Users\陈建辉\Documents\GitHub\selfteaching-python-camp\19100402\cjh20040088\d09\tang300.json','r',encoding='UTF -8') as f:
    txt=f.read()


print(stats_word.stats_text_cn(txt,100))
    