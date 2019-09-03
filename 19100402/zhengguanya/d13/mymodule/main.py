#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib as mpl
mpl.use('TkAgg')
#接受消息
import requests
import logging
logging.captureWarnings(True)
from wxpy import *
from pyquery import PyQuery
import stats_word
bot = Bot()
my_friend = bot.friends()  
@bot.register(my_friend,SHARING)    
def reply_my_friend(msg):    
    r = requests.get(msg.url)   
    document = PyQuery(r.text)  
    content = document('#js_content').text()
    stats = stats_word.stats_text_cn(content)

#统计词频
    stats_dic = dict(stats)
    words = []
    times = []
    for k,v in stats_dic.items():
        words.append(k)
        times.append(v)
    print(words,times)
#生成图表   
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.font_manager as fm
    zhfont1 = fm.FontProperties(fname='C:\Windows\Fonts\msyh.ttc')

    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.sans-serif'] = ['SimHei']

    np.random.seed(19680801)
    plt.rcdefaults()
    fig, ax = plt.subplots()

    y_pos = np.arange(len(words))
    error = np.random.rand(len(words))

    ax.barh(y_pos, times, xerr=error, align='center',color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(words,fontproperties=zhfont1)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('times')
    ax.set_title(u'词频统计',fontproperties=zhfont1)
    plt.savefig('plot.jpg')
    return msg.reply_image('plot.jpg')
embed()



