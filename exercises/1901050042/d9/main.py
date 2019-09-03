
import json

path = r'C:\Users\Administrator\Documents\GitHub\selfteaching-python-camp\exercises\1901050042\d9\tang300.json'
with open(path,'r',encoding='UTF-8') as f:
    a = f.read()

from mymodule.stats_word import stats_text_cn as cn

print(cn(a,100)) 
#任选一个函数用a测试参数类型检测是否成功
