#导入模块
import requests
from pyquery import PyQuery
from mymodule import stats_word
import getpass
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg


#提取链接信息，并将词频统计结果返回给好友
def get_msg(msg):
    msg_friend = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = PyQuery(msg_friend.text)
    content = document('#js_content').text()
    reply = dict(stats_word.stats_text(content,100))
    #将词频结果转换为图表
    num_list = list(reply.values)
    name_list = list(reply.keys)
    fig, ax = plt.subplots()
    plt.title('words frequency',color='black')
    ax.set_xlabel('words',color='blue')
    ax.set_ylabel('frequency',color='blue')
    ax.set_xticklabels(num_list)
    ax.barh(num_list,name_list)
    #保存图片
    plt.savefig('wordsfrequency.png')
    return 'wordsfrequency.png'



