import json

with open('tang300.json','r',encoding = 'UTF-8') as file:
    a = file.read()

from mymodule import stats_word_d09

print('输出词频最高的前100个汉字词频：{stats_text_cn(str,100)}') 
#任选一个函数用a测试参数类型检测是否成功

'''
from mymodule import stats_word_d09
with open('tang300.json','r',encoding = 'UTF-8') as file:
    load_dict = file.read()
try:
    stats_word_d09.stats_text_cn(load_dict,100)
except ValueError:
    print ("Catch you, the input type should be string! Check it please!")

'''