import d9_stats_word
import os
import json

#调用tang300.json文件
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json'),'r',encoding='utf-8') as f:
    text=f.read()
f.closed
#尝试执行文件，统计文件中汉字，并输出词频最高前100个词
try:
     print (d9_stats_word.stats_text_cn(text,100))
except ValueError:
    print('输入对象必须为字符串类型')


