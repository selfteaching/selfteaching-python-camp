

import json

path = r'C:\Users\khhsieh\Documents\GitHub\selfteaching-python-camp\exercises\1901090011\d09\tang300.json'
with open(path,'r',encoding='UTF-8') as f:
    a = f.read()

from mymodule.stats_word import stats_text_cn as cn

print(cn(a,100)) 
#任選一個函數用a測試參數類型檢測是否成功
