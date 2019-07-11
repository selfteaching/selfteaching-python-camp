import mymodule.stats_word as stats_word
import requests
from pyquery import PyQuery
import yagmail
import getpass

#coding:utf-8
import json
import requests
from wxpy import *

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from os import path

#登录缓存
bot = Bot(cache_path=True)

print('姜翔AI已经启动')

#绘制图表函数
def tabber(dic,path):

    plt.rcdefaults()
    fig, ax = plt.subplots()

    #取出字典里的key
    words_name = []
    words_value = []

    #取到纵坐标的labels，和横坐标的值
    for key,value in dic.items():
        words_name.append(key)
        words_value.append(value)

    y_pos = np.arange(len(words_name))
    #给横坐标赋值
    performance = words_value

    #设置字体
    font = FontProperties(fname='/Library/Fonts/Songti.ttc')
    #绘图
    b = ax.barh(y_pos, performance, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(words_name,FontProperties = font)
    ax.invert_yaxis()  #labels read top-to-bottom
    ax.set_xlabel('词 频 数 量',FontProperties = font)
    ax.set_title('词    频    分    析',FontProperties = font)

    #添加数据标签
    for rect in b:
        w=rect.get_width()
        ax.text(w,rect.get_y()+rect.get_height()/2,'%d'%int(w),ha='left',va='center')

    plt.savefig(path)
    
    #plt.show()

#自动词频统计机器人
def auto_ai(text,path):
    try:
        url = text
        response = requests.get(url,verify = False)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        #对列表中中英文字符，进行统计降序排列
        sort_list = stats_word.stats_text_cn(content,10)
        #返回绘图
        
        tabber(sort_list,path)
    
        #return str(sort_list)

    except ValueError as result:
        print(result)
    except:
       print('未识别的异常！')

cwd = path.abspath(path.dirname(__file__))
try:
    #回复 my_friend 的消息 (优先匹配后注册的函数!)
    #my_friend = bot.friends().search('东投')[0]
    #发送文本给好友
    #my_friend.send('在吗？回复下！')
    
    @bot.register(chats = [Friend])
    def forward_message(msg):
        print('[接收]'+str(msg))
        if (msg.type!='Text'):
            image_path = path.join(cwd,'day13.png')
            auto_ai(msg.url,image_path)
            msg.reply_image(image_path)
            #return '稍等，正在给分析词频！\n' + auto_ai(msg.url)
        else:
            print('[发送]'+'很不错！')
            return '很不错!'

    #持续监听好友
    embed()
except:
    print("该好友不存在！")
 




