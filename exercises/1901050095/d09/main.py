import json
#JSON(JavaScript Object Notation, JS 对象标记) 是一种轻量级的数据交换格式。JSON的数据格式其实就是python里面的字典格式，里面可以包含方括号括起来的数组，也就是python里面的列表。
count=int()
path = r'C:\Users\Administrator\Documents\GitHub\selfteaching-python-camp\exercises\1901050095\d09\tang300.json'
with open(path,'r',encoding='UTF-8') as f:
    a = f.read()
from mymodule.stats_word import stats_text_cn
print(a,100) 
#任選一個函數用a測試參數類型檢測是否成功