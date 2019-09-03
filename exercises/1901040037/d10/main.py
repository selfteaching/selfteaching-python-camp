#-*- coding:utf-8 -*-
from mymodule import stats_word 
import json
from collections import Counter

with open("/Users/pecky/Desktop/02 自学营python/selfteaching-python-camp/exercises/1901040037/d09/tang300.json", 'r') as f:
    poems = json.loads(f.read())

words = []#每一句诗单独把诗都拿出来，存在一个列表里
for poem in poems:
    words.append(poem['contents']) 
   # print(poem['contents'])
#print(words)

all_charter = ''
for word in words:
    all_charter += word

stats_word.stats_text_cn(all_charter)

Counter(all_charter).most_common(10)

# test1 = 3.1415926  # 用 try except 捕获异常并执行
# try:
#     stats_word.stats_text(test1)
# except ValueError:
#     print("大哥，要输入文本啊")
# except TypeError:
#     print("大姐，要输入文本啊，你输错啦")

# text = '''
# 愚公移山
# @@ -49,3 +56,8 @@
# '''

# stats_word.stats_text(text)

#sw.stats_text_cn(1) #测试触发异常
#sw.stats_text_en(1) #测试触发异常
#sw.stats_text(1)    #测试触发异常