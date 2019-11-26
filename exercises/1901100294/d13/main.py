from mymodule import stats_word
import requests
from pyquery import PyQuery
import matplotlib.pyplot as plt
import numpy as np
from pyecharts import Bar



def get_article():
    url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
    r = requests.get(url)
    document = PyQuery(r.text)
    article_str = document('#js_content').text()
    result = stats_word.stats_text_cn(article_str, 10)
    return result  

paixu = get_article()
paixu_list = []

for paixu_tuple in paixu:
    for paixu_str in paixu_tuple:
        paixu_list.append(paixu_str)

name = paixu_list[::2] #取出所有名字
number = paixu_list[1::2] #取出所有对应的词频数


bar = Bar('词频输出')
bar.add('词频',name,number)
bar.show_config()
bar.render()