#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

plt.rcdefaults()
fig,ax = plt.subplots()
# 设置中文字体  # issue#1692 provided another solution on font setting problems pyplotz: pip install
cnfont = fm.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

# 定义绘制图标函数并保存为图片
def chartImg(data={}) :
    print('process img start')
    group_x = list(data.values())
    group_y = list(data.keys())
    # 自定义表格标签及标题样式
    plt.title('词频统计表',color='black',fontproperties = cnfont,fontsize = 16) #ax.set_title ? copied @slona-song's code a
    ax.set_xlabel('数量',fontproperties = cnfont, color = 'grey')
    ax.set_ylabel('词语',fontproperties = cnfont, color = 'grey')
    # 绘制图表
    ax.set_yticklabels(group_y,fontproperties = cnfont)
    ax.barh(group_y,group_x)
    # 保存绘制文件
    plt.savefig('chart.png')
    print('process img done')
    return 'chart.png'


from mymodule import stats_word as sw
import requests
from pyquery import PyQuery
#from wxpy import * error notification resolved by issue #1169
from wxpy import *

bot = Bot(cache_path=True)

@bot.register()
def auto_reply(msg):
    if msg.type == SHARING:
        response = requests.get(msg.url)  # msg.url为分享的网址
        document = PyQuery(response.text)
        content = document('#js_content').text()
        # 像d11一样处理文本
        result = dict(sw.stats_text_cn(content, count=10))
        print('process text done')
        msg.reply_image(chartImg(result)) #回复刚才保存的图片给好友      

embed()
# bot.join()

# url  = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
# response = requests.get(url)  # msg.url为分享的网址
# document = PyQuery(response.text)
# content = document('#js_content').text()
# result = sw.stats_text_cn(content, count=10)

# chartImg(dict(result))