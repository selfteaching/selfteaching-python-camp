
import jieba 
import re # 调用正则表达式模块
from mymodule import stats_word
import json

with open('D:\\Documents\\GitHub\\selfteaching-python-camp\\exercises\\1901060008\\d09\\tang300.json', 'r',encoding='UTF-8') as f:
    t=json.load(f)       #读取文件
stats_word.stats_text_cn(t,20)      #调用模块

    
    


  
