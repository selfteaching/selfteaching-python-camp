import matplotlib.pyplot as plt
import numpy as np

from wxpy import *
from collections import Counter
import jieba
import pyquery
import requests


bot=Bot()    #初始化机器人，扫码登陆微信网页版
my_friend = bot.friends()  #回复对象为所有好友

#回复 my_friend 发送的消息
@bot.register(my_friend, SHARING)    #接收分享（SHARING）类型消息
def reply_my_friend(msg):
    r = requests.get(msg.url)    #msg.url为分享类型消息的网页链接
    r.text
    from pyquery import PyQuery
    document = PyQuery(r.text)
    content = document('#js_content').text()
    import stats_word1
    result = stats_word1.stats_text_cn(content, 10)
    result_str =  ' '.join([ str(i) for i in result ])

    np_list=np.array(result) #将文本处理结果转化为二维数组
    word_list=[] #初始化盛放词的列表
    word_frequency_list=[] #初始化盛放词频的列表
    for i in range(len(np_list)): #拆分Numpy多维数组
        word_list+=[np_list[i][0]]
        #Numpy在处理('a',8)的时候，会把8记录为'8'，所以需要强制转换类型为int
        word_frequency_list+=[int(np_list[i][1])]

    plt.rcParams['font.sans-serif']=['SimHei']    #用来正常显示中文标签
    index = np.arange(len(word_list))
    fig, ax = plt.subplots()
    ax.barh(index, word_frequency_list, align='center', color='green', ecolor='black')
    ax.set_yticks(index)
    ax.set_yticklabels(word_list)
    ax.invert_yaxis()
    ax.set_xlabel('word frequency')
    ax.set_title('The word frequency of this article')

    plt.savefig('word_frequency.png')    #保存绘图
    msg.reply_image('word_frequency.png')    #回复绘图

embed()    #堵塞线程，让程序保持运行，保持监听状态
