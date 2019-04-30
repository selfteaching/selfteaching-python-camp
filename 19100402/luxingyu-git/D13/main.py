from mymodule import stats_word
from pyquery import PyQuery
import requests
from wxpy import *  # 导入模块
import matplotlib.pyplot as plt
import numpy as np


bot = Bot() # 初始化机器人，扫码登陆
my_friend = bot.friends().search('阿雙')[0] # 搜索名称含有 "阿雙" 的好友
# 发送文本给好友
my_friend.send('你好! 请分享一篇公众号文章给我，我来给你统计下文章中用到最多的前20个词语。')

@bot.register(my_friend)
def my_friend_SHARING(msg):
    msg = requests.get(msg.url)
    document = PyQuery(msg.text)        
    content = document('#js_content').text()   
    str1 = dict(stats_word.stats_text_cn(content,20))
    '''my_friend.send(str1)'''
    np.random.seed(19680801)
    plt.rcdefaults()
    fig, ax = plt.subplots()
    word = []
    frequency = []
    for i in str1:
        word.append(i)
        frequency.append(str1[i])

    y_pos = np.arange(len(word))
    error = np.random.rand(len(word))
    plt.rcParams['font.sans-serif'] = ['SimHei'] #添加中午字体避免显示问题

    ax.barh(y_pos, frequency, xerr=error, align='center',color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(word)
    ax.invert_yaxis()
    ax.set_xlabel('词语出现次数')
    ax.set_title('词频统计')

    plt.savefig('words_frequency.png') # 将结果保存为图片文件
    msg.reply_image('words_frequency.png') # 将图片发送给好友

embed() # 进入 Python 命令行、让程序保持运行