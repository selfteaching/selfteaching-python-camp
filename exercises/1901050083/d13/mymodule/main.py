import stats_word
import re
import json
from os import path
import requests
from pyquery import PyQuery
import yagmail
from wxpy import *
import matplotlib.pyplot as plt

bot = Bot(cache_path = True)
my_friend = bot.friends().search('那个谁')[0]
@bot.register(my_friend, except_self = False)


def auto_reply(msg):
    print (msg.sender.name,':',msg.text,'Msg Type:',msg.type, msg.url)
    msg.sender.mark_as_read()
    if msg.type == SHARING:
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        count=20
        most_20=stats_word.stats_text_cn(content, count)
        
        word=tuple(dict(most_20))
        values=tuple(dict(most_20).values())
        
        fig, ax = plt.subplots() # 不知道是什么

        plt.barh(word, values, height=0.7, color='steelblue', alpha=0.8) #生成图表

        ax.set_yticks(word)
        ax.set_yticklabels(word)#纵轴
        ax.invert_yaxis()  # 从上到下
        ax.set_xlabel('次数')#横轴
        ax.set_title('刚才那篇文章出现次数最多的前20个词是')#标题

        for x, y in enumerate(values):
            plt.text(y + 0.1, x + 0.3, '%s' %y) #数字

        plt.savefig('day13.png')
        msg.reply_image('day13.png')
        
embed()

 

