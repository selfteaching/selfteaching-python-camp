from mymodule import stats_word
import logging
import yagmail
import requests
import getpass
import pyquery
from pyquery import PyQuery
from wxpy import *

import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
import matplotlib




bot = Bot()

@bot.register(msg_types = SHARING)# 自动接受新的好友请求

def reply_my_friend(msg):
    r = requests.get(msg.url)#使⽤requests请求信息中的url
    document = pyquery.PyQuery(r.text)
    contents = document('#js_content').text()#将response.text用pyquery把链接中内容提取出来
    
    #处理文本，为绘图准备
    result = str(stats_word.stats_text_cn(contents,30))
    #使⽤用stats_word中的stats_text对提取结果进⾏行行分析和词频统计处理理(返回前30个词的 统计结果)
    result = eval(result)
    
    word =[] # 将所有的单词取出组成一个元组
    counts =[] # 将所有的词频取出组成一个列表
    for item in result:
        word.append(item[0])
        counts.append(item[1])
    word = tuple(word)
   
    #绘图
    # frot = FontProperties(fname=r"c:\windows\fonts\AcadEref.ttf", size=8)
    # myfont = matplotlib.font_manager.FontProperties(fname="Light.ttc")#使用matplotlib画图的时候，有可能会遇到中文显示小框框，无法正常显示，下面提供一下解决办法。
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

    # plt.rcdefaults()
    fig, ax = plt.subplots()

    y_pos = np.arange(len(word))# y_pos为y轴的坐标，这里就是有几条柱状图的意思。
    counts = np.array(counts)# counts 是条的宽度
    error = np.random.rand(len(word))

    ax.barh(y_pos, counts, xerr=error, align='center',
    color='green', ecolor='black')
    """
    ecolor 容错条的颜色
    xerr为容错值。就是柱状顶端的小黑线。可以不设置
    align 对齐方式
    color 条的颜色
    """
    ax.set_yticks(y_pos)# 设置 y 轴的命名位置，需要跟下面的 set_yticklabels 配合使用
    
    ax.set_yticklabels(word)# 设置 y 轴的标签名称
    
    ax.invert_yaxis() ## 反转 y 轴 labels read top-to-bottom
    ax.set_xlabel('词频counts')
    ax.set_title('文章词频统计Analysis of Chinese word frequency')
    plt.savefig('d13.jpg')# 保存图像
    # plt.show()# 显示图像

    msg.reply_image('d13.jpg')#将处理结果返回给发送消息过来的好友

embed()




