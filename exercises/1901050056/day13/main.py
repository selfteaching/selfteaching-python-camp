from mymodule import stats_word
from pyquery import PyQuery
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np
import json
import requests
import pyquery


bot = Bot()
#find friend
my_friend = bot.friends()
print(my_friend)


#monitor and auto_reply all_firend message
# @bot.register()
# def print_others(msg):
#     print(msg) 
#     msg.reply(msg)

@bot.register(my_friend,SHARING) #接收sharing信息
def auto_reply(msg):
    sharing_text = requests.get(msg.url) 
    document = PyQuery(sharing_text.text)
    content = document('#js_content').text()
    s1 = stats_word.stats_text(content,10)
    s2= dict(s1) #字典化
    keys,values = zip(*s2.items()) #拆分单词和统计字数
   
    plt.rcdefaults()
    fig,ax = plt.subplots()
        # Example data
    people = s1
    y_pos = np.arange(len(people))
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))
    word_frequency = values

    plt.rcParams['font.sans-serif']=['SimHei'] #不用这行会出现中文字变框框，windows平台可用
    ax.barh(y_pos, word_frequency, xerr=error, align='center',color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(keys)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('次数')
    ax.set_title('文章高频词统计如下')
    plt.savefig('day13.png')
    msg.reply_image('day13.png')

embed()
