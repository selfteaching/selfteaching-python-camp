# 1901050017 day13 sarah
# 将实战项目2中的结果生成一张图表文件
# 用图标文件替代之前发送的文本
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import requests
import matplotlib.pyplot as plt

from os import path
from pyquery import PyQuery
import stats_word
from wxpy import *

# input a weixin's article url, and then return a sorted word dict.
def sort_text(url):
    response = requests.get(url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    return stats_word.stats_text_cn(content, 10)


    # input text and define output word numbers


def save_as_image(sorted_dict):
    plt.rcdefaults()
    fig, ax = plt.subplots()
    
    words = [x for (x, y) in sorted_dict]
    count = [y for (x, y) in sorted_dict]   

    ax.barh(words, count, align = "center", color = "blue")
    ax.set_yticks(words)
    ax.set_yticklabels(words)
    ax.invert_yaxis()
    ax.set_xlabel('count')
    ax.set_title('Top 10 words sorted by frequency')
    plt.savefig('result.png')
    plt.show()
    return 'result.png'



bot = Bot()
my_friend = bot.friends()

# auto reply SHARING message.
@bot.register(my_friend, SHARING)
def reply_my_friend(msg):
    sorted_dict = sort_text(msg.url)
    save_as_image(sorted_dict)

    print(msg.sender)
    return 'result.png'

embed()



