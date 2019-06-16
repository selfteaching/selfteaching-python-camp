
import jieba 
from mymodule import stats_word
import requests
from pyquery import PyQuery
import getpass
import yagmail
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np 

bot=Bot()            #登录微信
friend=bot.friends().search('test')[0]        #寻找好友
friend.send('send me file please!')           #发送消息给好友（此项可以省掉）


@bot.register(Friend,SHARING)
def replfriy_end(msg):                   #定义一个新函数
    response=requests.get(msg.url)       #从所给的链接获取数据
    document=PyQuery(response.text) 
    content=document('#js_content').text()
    result= stats_word.stats_text(content,5)
    result_dict=dict(result)
    word=[]
    number=[]
    for i in result_dict:
        word.append(i)
        number.append(result_dict[i])

    plt.rcdefaults()
    fig , ax = plt.subplots()

    y=np.arange(len(word))
    error=np.random.rand(len(word))

    plt.rcParams['font.sans-serif'] = ['SimHei']         #将中文字体显现
    ax.barh(y,number,xerr=error,align='center',color='red')
    ax.set_yticks(y)
    ax.set_yticklabels(word)

    ax.invert_yaxis()
    ax.set_xlabel('出现次数') 
    ax.set_title('词频统计表')

    plt.savefig('day13.png')
    msg.reply_image('day13.png')  
embed()
    


  
