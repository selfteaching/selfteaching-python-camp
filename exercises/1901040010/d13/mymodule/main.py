

from stats_word import stats_text_cn
import requests
from pyquery import PyQuery
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
fig, ax = plt.subplots()

def draw_bar_chart(xword,yquantity):
    plt.rcParams['font.family']='sans-serif'
    plt.rcParams['font.sans-serif']='SimHei' #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
  
    ax.bar(range(len(yquantity)),yquantity,tick_label = xword)
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Word')
    ax.set_title('What are the 20 most used words in this article?')

    plt.savefig('/Users/min/Documents/frcy.jpg')
    plt.show()


from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()
my_friend = bot.friends().search()
@bot.register(chats=my_friend,msg_types=SHARING,except_self=True,run_async=True,enabled=True)


def friend_sharing(msg):
    response = requests.get(msg.url) 
    document = PyQuery(response.text) 
    content = document('#js_content').text()
    result = stats_text_cn(content,20)
    
    word_list = []
    quantity_list = []
    for x in result:
        word_list.append(x[0])
        quantity_list.append(x[1])

    draw_bar_chart(word_list,quantity_list)

    msg.sender.send_image('/Users/min/Documents/frcy.jpg')

embed()


   