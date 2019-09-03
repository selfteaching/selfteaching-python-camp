import matplotlib.pyplot as plt
import numpy as np
from pyplotz.pyplotz import PyplotZ 
import requests
from pyquery import PyQuery
import sys
sys.path.append("/Users/zhangdequan/Documents/GitHub/selfteaching-python-camp/19100302/DequanZhang/mymodule")
from stats_word import stats_text_cn

from wxpy import *

bot = Bot()
myfriend = bot.friends()

@bot.register(myfriend, msg_types=SHARING)  #消息为SHARING类型时，获取消息的网页链接msg.url，自动返回词频统计结果
def reply_my_friend(msg):
    response = requests.get(msg.url)    
    document = PyQuery(response.text)
    content = document('#js_content').text()
    statlist = stats_text_cn(content,100)
    #绘图：
    result=np.array(statlist) 
    word_list=[] 
    number_list=[] 
    for i in range(len(statlist)): 
        word_list+=[result[i][0]]
        number_list+=[int(result[i][1])] 
    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos = np.arange(len(word_list))
    ax.barh(y_pos, number_list, align='center', color='yellow', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(word_list)
    ax.invert_yaxis()
    ax.set_xlabel('词频')
    ax.set_title('分享文章词频统计top20')
    plt.savefig("stats.png") 
    plt.show()

    msg.reply_image('stats.png')


embed()   #进入Python命令行，让程序保持运行
