from mymodule import stats_word as sw
import requests
from pyquery import PyQuery
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np
bot = Bot() #扫码登录微信

my_friend = bot.friends() #定义好友变量

@bot.register(my_friend,SHARING) #接收share类信息
def auto_reply(msg):
    
    msg_from_friend = requests.get(msg.url) 
    document = PyQuery(msg_from_friend.text)
    content = document('#js_content').text()
    #URL信息提取
    reply = dict(sw.stats_text(content,count=100))
    num_list=list(reply.values)
    name_list=list(reply.keys)

    fig, ax = plt.subplots()
    # 自定义表格标签及标题样式
    plt.title('Frequency summary',color='black',fontsize = 16)
    ax.set_xlabel('frequency', color = 'grey')
    ax.set_ylabel('words', color = 'grey')

    ax.set_yticklabels(num_list)
    ax.barh(num_list,name_list)

    plt.savefig('words_frequency.png')
    return 'words_frequency.png'

embed() #保持监听状态

