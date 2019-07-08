
#<<<<<<< master
# -*- coding: utf-8 -*-
# 读取本地唐诗三百首文件中的内容，并统计其中汉字的词频，输出词频最高的前100个词 
from collections import Counter 
# from  mymodule import stats_word
path = "exercises/1901050107/d09/tang300.json"

with open(path) as f:
    data = f.read()        
chars = []
# cnt = Counter()
for item in data:
    if isinstance(data,str):
        ValueError("data not a string ")

#=======
path = "exercises/1901050107/d09/tang300.json"
import os
from mymodule import stats_word
with open(path) as f:
    data = f.read()
 
from collections import Counter
chars = []
cnt = Counter()
for item in data:
#>>>>>>> master
    if '\u4e00' <= item <= '\u9fff':
        chars.append(item)
print(Counter(chars).most_common(100))   
