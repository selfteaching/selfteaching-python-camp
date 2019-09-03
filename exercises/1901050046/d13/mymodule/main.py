#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery
from wxpy import *

import stats_word

import matplotlib.pyplot as plt
import numpy as np

bot = Bot()
friend_name = input('请输入好友的备注名:')
my_friend =bot.friends().search(friend_name)[0]

@bot.register(my_friend, msg_types='Sharing')
def print_messages(msg): 
    #提取Sharing类型文章的正文
    r = requests.get(msg.url)
    document = PyQuery(r.text)
    content = document('#js_content').text()
    #统计词频
    result = stats_word.stats_text_cn(content,10,len_size = 2)
    print(result)
    result_words_list = []
    result_fre_list= []
    for i in range(len(result)):
        result_words_list.append(result[i][0])
        result_fre_list.append(result[i][1])

    #画图
    plt.rcdefaults()
    fig, ax = plt.subplots() #ax代替plt.subplots()

    y_pos = np.arange(len(result_words_list)) #设置y轴刻度的序列，即y轴上应该有几个点
    plt.rcParams['font.sans-serif']=['SimHei'] #解决图像不现实中文的问题
    ax.barh(y=y_pos, width=result_fre_list,align='center') #配置条形图
    ax.set_yticks(y_pos) #设置y轴刻度序列
    ax.set_yticklabels(result_words_list) #设置y轴刻度序列的名称
    ax.invert_yaxis()  # labels read top-to-bottom y轴的词频从上到下依次为从大到小排列
    ax.set_xlabel('词频数')#设置x轴名称
    ax.set_title('出现次数最多的10个词') 
    plt.savefig('DAY13.jpg')

    msg.reply_image('DAY13.jpg')

embed()
