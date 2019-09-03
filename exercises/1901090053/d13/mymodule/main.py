
import stats_word as sw 
import json
from pyquery import PyQuery
import requests
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm


bot = Bot(cache_path=True)
my_friend = bot.friends().search('测试员')[0]
#my_friend = bot.file_helper
@bot.register(my_friend)
def auto_reply_word_stats(msg):
    #print(msg)
    r = requests.get(msg.url)
    document = PyQuery(r.text)
    text = document('p').text()
    r = requests.get(msg.url)
    document = PyQuery(r.text)
    text = document('p').text()
    plt.rcdefaults()
    fig, ax = plt.subplots()
    contents = sw.stats_text_cn(text, 10)
    words = tuple(contents.keys())
    y_pos = np.arange(len(words))
    frequence = list(contents.values())
    ax.barh(y_pos, frequence, align='center')
    ax.set_yticks(y_pos)
    myfont = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
    ax.set_yticklabels(words, fontproperties=myfont)
    ax.invert_yaxis()
    ax.set_xlabel('Frequence')
    ax.set_title('Frequence of Words in the Article',fontproperties=myfont)
    fig.savefig('plot.png')
    my_friend.send_image('plot.png')


bot.join()
bot.logout()
