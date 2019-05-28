import collections
import jieba
import re#导入正则表达式模块
import requests
from wxpy import *
from pyquery import PyQuery
import matplotlib.pyplot as plt
import numpy as np
def stats_text_en(text):
    f = lambda x: x.split(" ")
    text= text.lower()
    text=re.sub("[^\\u0061-\u007a]", " ", text)#小写字母unicode范围，筛选英文
    text=text.split()#指定分隔符对字符串进行切片
    found=[]
    for x in text:
        if len(x)>=2:
            found.append(x)
    word_counts= collections.Counter(found).most_common(10)
    word_counts=dict(word_counts)

    np.random.seed(19680801)
    plt.rcdefaults()
    fig, ax = plt.subplots()
    print(word_counts)

# Example data
    counter_list = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    label = list(map(lambda x: x[0], counter_list[:20]))
    value = list(map(lambda y: y[1], counter_list[:20]))
    plt.bar(range(len(value)), value, tick_label=label)
    plt.savefig('chart.jpg')
    return 'chart.jpg'

            


