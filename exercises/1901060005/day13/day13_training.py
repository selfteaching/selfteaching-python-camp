# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()
my_friend = bot.friends()
# 发送文本给好友
#my_friend.send('Hello WeChat!')

from pyquery import PyQuery
import yagmail
import getpass
import requests
from mymodule import d11_stats_word as sw
import matplotlib.pyplot as plt
import numpy as np

@bot.register(my_friend,SHARING) #接受share类信息
def reply_my_friend(msg):
    response = requests.get(msg.url)   
    document = PyQuery(response.text)    
    content = document('#js_content').text()
    #URL信息提取
    reply = sw.stats_text(content,10)
    #return reply
    #print(reply)
    #np_list=np.array(result) #将文本处理结果转化为二维数组
	
    reply_dict=dict(reply)
    word=[]
    number=[]
    for i in reply_dict:
        word.append(i)
        number.append(reply_dict[i])

    plt.rcdefaults()
    fig , ax = plt.subplots()

    y=np.arange(len(word))
    error=np.random.rand(len(word))

    plt.rcParams['font.sans-serif'] = ['SimHei']         #将中文字体显现
    ax.barh(y,number,xerr=error,align='center',color='green')
    ax.set_yticks(y)
    ax.set_yticklabels(word)

    ax.invert_yaxis()
    ax.set_xlabel('出现次数') 
    ax.set_title('分享文章词频统计')

    plt.savefig('day13.png')
    msg.reply_image('day13.png')  
embed()
          





