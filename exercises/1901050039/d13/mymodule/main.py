from wxpy import *
import requests
from pyquery import PyQuery
import stats_word
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
bot = Bot()

@bot.register()   #回复信息
def auto_reply(msg): 
    if msg.type == 'Sharing':    #设条件，是微信公号文章的就进行词频分析
        r = requests.get(msg.url)
        document = PyQuery(r.text)
        content = document('#js_content').text()
        res2 = dict(stats_word.stats_text_cn(content))
        x = tuple(res2.keys())   #制表
        y = tuple(res2.values())
        plt.bar(x,y,width=0.5)
        plt.title("高频词汇表")
        plt.xlabel("高频词汇")
        plt.ylabel("次数")
        plt.savefig('list.png')    
        return msg.reply_image('list.png')
    else:
        print(msg)
embed()