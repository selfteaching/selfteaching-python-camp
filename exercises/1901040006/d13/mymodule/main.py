import stats_word
import requests
from pyquery import PyQuery as pq
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np

bot = Bot()

@bot.register(Friend, SHARING)
def auto_reply(msg):
    r = requests.get(msg.url)
    document = pq(r.text)
    content = document('#js_content').text()
    #统计词频
    result = stats_word.stats_text(content,0,10)
    #画布
    plt.rcdefaults()
    fig, ax = plt.subplots()
    #处理数据
    people = list(dict(result).keys())
    y_pos = np.arange(len(people))
    performance = list(dict(result).values())
    #设置字体
    plt.rcParams['font.sans-serif']=['SimHei']
    #画图
    ax.barh(people, performance, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Performance')
    ax.set_title('TOP10词频统计')
    plt.savefig('day13.png')
    #回复图片
    msg.reply_image('day13.png')

embed()