from wxpy import *
import requests
from pyquery import PyQuery
import numpy as np
import matplotlib.pyplot as plt
import stats_word
plt.rcParams['font.family']=['SimHei']

bot = Bot()

@bot.register()   #回复信息
def auto_reply(msg): 
    if msg.type == 'Sharing':    #设条件，是微信公号文章的就进行词频分析
        r = requests.get(msg.url)
        document = PyQuery(r.text)
        content = document('#js_content').text()
        result = dict(stats_word.stats_text_cn(content))
        x = tuple(result.keys())
        y = tuple(result.values())
        plt.bar(x,y,width=0.5)
        plt.xlabel(u"高频词汇")
        plt.ylabel(u"频次")
        plt.title("高频词汇统计表")
        plt.ylim(0,int(y[0]))
        plt.savefig('my_result.png')
        plt.show()
    return ('my_result.png')

embed()
