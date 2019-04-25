from wxpy import *
import requests
from pyquery import PyQuery
import stats_word
import numpy 
import matplotlib.pyplot as plt
plt.rcParams['font.family']=['SimHei']
bot = Bot()

@bot.register()   #回复信息
def auto_reply(msg): 
    if msg.type == 'Sharing':    #设条件，是微信公号文章的就进行词频分析
        r = requests.get(msg.url)
        document = PyQuery(r.text)
        content = document('#js_content').text()
        result = dict(stats_word.stats_text_cn(content))  #把结果变成字典
        x = tuple(result.keys())
        y = tuple(result.values())
        plt.bar(x,y,width=1.0)
        plt.title("高频词汇表")
        plt.xlabel("高频词汇")
        plt.ylabel("次数")
    return plt.show()

embed()