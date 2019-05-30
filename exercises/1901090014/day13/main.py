import requests  
from pyquery import PyQuery  
from models.stats_word_13 import *
from wxpy import *  

import matplotlib.pyplot as plt  
import numpy as np   


bot = Bot(cache_path=True) #扫码登录
my_friend = bot.friends()  # 好友
@bot.register(my_friend,SHARING) #监听

def print_friend_messages(msg):
    response=requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    count= 10 
    my_list= stats_text_cn(content,count)   # 统计中文词频
    my_dict = dict(my_list)  


    plt.rcdefaults()    
    fig, ax = plt.subplots()    

    plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签  
    plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

    jl_list = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    label = list(map(lambda x: x[0], jl_list[:20]))
    value = list(map(lambda y: y[1], jl_list[:20]))

    # 水平直方图
    ax.barh(range(len(value)), value, tick_label=label, align='center',  color='green')     

    ax.set_xlabel('出现次数')    # X轴标签
    ax.set_ylabel('文字')    # Y轴标签
    ax.set_title('文章统计图')    # 标题
    plt.savefig('stats.png')    
   
    msg.reply_image('stats.png')  # 给好友回复图片
        

embed() # 进入Python命令行，让程序保持运行


