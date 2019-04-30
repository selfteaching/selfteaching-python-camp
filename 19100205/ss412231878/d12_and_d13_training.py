#这是把day12与day13合并的代码
from wxpy import *
from pyquery import PyQuery
import requests
from mymodule import stats_word
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import random as rd

def counter_stats(list_a):#这里接收词频的统计结果
    word = []
    number = []
    for i in list_a:
        word.append(i[0])
        number.append(i[1]) #以上重新把词频统计结果拆分到图片生成的x和y轴
    
    plt.rcdefaults()
    fig,ax = plt.subplots()

    counter = word
    y_counter = np.arange(len(counter))
    counter_number = np.array(number)

    mpl.rcParams['font.sans-serif'] = ['SimHei']   #设置简黑字体
    mpl.rcParams['axes.unicode_minus'] = False     #解决-的问题
    ax.barh(y_counter,counter_number,align='center',color='pink',ecolor='black')
    ax.set_yticks(y_counter)
    ax.set_yticklabels(counter)
    ax.invert_yaxis()
    ax.set_xlabel('Counter')
    ax.set_title('Counter_stats_word')#以上是定义生成的图片

    path = 'C:\\Users\\33\\' + str(rd.randint(1,100)) + '.png'
    print(path)
    plt.savefig(path)#以上保存图片成一个随机1-100的文件名，不这样的话只能执行一次
    return path

def main():#这里与最后的命名保持一致
    bot = Bot()#登录微信的命令
    my_friend = bot.friends()#发给所有好友
               
    @bot.register(msg_types=SHARING)#接收分享类信息
    def reply_my_friend(msg):
         
        wechat = requests.get(msg.url)
        document = PyQuery(wechat.text)
        content = document('#js_content').text()
        list_a = stats_word.stats_text(content)#接收发来的分享链接的文字，并处理成词频统计结果
           
        msg.reply_image(counter_stats(list_a)) #回复刚才保存的图片给好友        
        return

    embed()#让程序执行到这里后返回，以便于重新执行

if __name__=='__main__':#这条语句能够帮助windows正常系统执行上面部分代码
    main()