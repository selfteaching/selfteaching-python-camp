import requests
import stats_word as sw
from pyquery import PyQuery as py
from wxpy import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties #为了显示中文，替换字体

bot = Bot()
my_friend = bot.friends()

@bot.register(my_friend,SHARING)
def auto_reply(msg):
        response = requests.get(msg.url)
        document = py(response.text)
        content = document('#js_content').text()
        result = sw.stats_text_cn(content,30)
        #print(result)
        np_list = np.array(result)
        word_list = [] #初始化盛放词的列表
        number_list = [] #初始化盛放词频的列表
        for i in range(len(np_list)):
                word_list += [np_list[i][0]]
                number_list += [int(np_list[i][1])]
        
        #print(word_list)
        #print(number_list)

        font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=8)

        plt.rcdefaults() #重置rc所有参数，类似初始化
        fig,ax = plt.subplots() #建立一个子图对象

        y_pos = np.arange(len(word_list)) #y_os为y轴的坐标

        ax.barh(y_pos,number_list,align='center',color='green',ecolor='black')
        #生成一个水平的条形图
        #y_pos为y轴的坐标
        #number_list是条的宽度
        #align为对齐方式
        #color为条的颜色
        #ecolor为容错条的颜色
        ax.set_yticks(y_pos) #设置y轴的名称需要和下面的set_yticklabels配合使用
        ax.set_yticklabels(word_list,fontproperties=font)
        ax.invert_yaxis() #反转y轴
        ax.set_xlabel('词频',fontproperties=font)
        ax.set_title('好友分享链接统计词频的图片',fontproperties=font)
        plt.savefig("stats.png") #保存图片
        msg.reply_image("stats.png") #回复图片

embed()

        