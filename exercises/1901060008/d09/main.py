
from collections import Counter   #调用collections模块
import re # 调用正则表达式模块
import time


with open('D:\\Documents\\GitHub\\selfteaching-python-camp\\exercises\\1901060008\\d09\\tang300.json', 'r',encoding='UTF-8') as f:

    t=f.read()
    
    print('打印唐诗三百首：\n',t)
    t1=re.findall(r'[\u4e00-\u9fa5]',t)
    # print(t1)
    count=Counter(t1).most_common(20)
    print('打印出现次数最多的二十个汉字：\n',count)

  
