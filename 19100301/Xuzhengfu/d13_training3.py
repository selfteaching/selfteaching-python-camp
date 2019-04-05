#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib as mpl
mpl.use('TkAgg')
# 接受消息、提取文本
import requests
from wxpy import *
from pyquery import PyQuery
from day12 import stats_word as sw

bot = Bot()
my_friend = bot.friends()

@bot.register(my_friend,SHARING)
def reply_my_friend(msg):
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    stats = sw.stats_text(content,10)

# 统计数据
    stats_dict=dict(stats)
    keyword=[]
    keyword_num=[]
    for x in stats_dict:
        keyword.append(x)
        keyword_num.append(stats_dict[x])

# 根据统计结果生成图表
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.font_manager import FontManager, FontProperties
    cnfont = FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')
    
    np.random.seed(19680801)

    plt.rcdefaults()
    fig, ax = plt.subplots()

    y_pos = np.arange(len(keyword))
    error = np.random.rand(len(keyword))

    ax.barh(y_pos, keyword_num, xerr=error, align='center', color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(keyword,fontproperties = cnfont,color='black')
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Occurrence Number')
    ax.set_title('The ten most frequently used words')
    plt.savefig('/Users/xuzhengfu/Documents/GitHub/stats_result.png')
    
# 回复统计图表给好友
    return msg.reply_image('/Users/xuzhengfu/Documents/GitHub/stats_result.png')
embed()