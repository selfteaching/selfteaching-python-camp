from wxpy import *
from pyquery import PyQuery
import requests
from stats_word import stats_text_cn
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties  
bot=Bot(True)               #启动web微信，设置为True值可以在短时间内不用重复扫码登录
bot.enable_puid()           #不知道干什么用的，但是加入这条命令，就可以在Python里监控微信里收到的信息

friends=bot.friends()

# 打印/监控来自其他好友、群聊和公众号的消息
@bot.register()#参数为空时，默认为所有人
def print_others(msg):
    print(msg)
    

@bot.register(friends,SHARING)  #SHARING是message类型
def print_link(msg):           
    print('网页链接地址:',msg.url,'\n','发信人:',msg.sender)
    response=requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14) 
    ref=stats_text_cn(content,10)
    word=[]
    count=[]
    for i in ref:
            word.append(i[0])
            count.append(i[1])
    np.random.seed(19680801)
    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos = np.arange(len(word))
    ax.barh(y_pos, count, align='center',color='green')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(word,fontproperties=font)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('次数',fontproperties=font)
    ax.set_title('最常见的10个中文词汇以及出现次数',fontproperties=font)
    plt.savefig('d13.png')
    msg.reply_image('d13.png')

    

embed()