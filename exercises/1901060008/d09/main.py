
from collections import Counter   #调用collections模块
import re # 调用正则表达式模块
import time


with open('D:\\Documents\\GitHub\\selfteaching-python-camp\\exercises\\1901060008\\d09\\tang300.json', 'r',encoding='UTF-8') as f:
    # for line in f.readlines():
    #     print(line)
        # time.sleep(1)
    t=f.read()
    
    print('打印唐诗三百首：\n',t)
    t1=re.findall(r'[\u4e00-\u9fa5]',t)
    count=Counter(t1).most_common(100)
    print('打印出现次数最多的一百个汉字：\n',count)

  
