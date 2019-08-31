import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from mymodule import stats_word
import requests
from pyquery import PyQuery
from wxpy import *

def main():
    bot = Bot() #扫描二维码登录微信
    my_friend = bot.friends() #回复对象为所有好友

    @bot.register(my_friend,SHARING) #接受分享类消息
    def auto_reply(msg):
        response = requests.get(msg.url) #msg.url为分享的网址
        document = PyQuery(response.text)
        content = document('#js_content').text()
        
        #处理文本：
        #如果输出100个结果，图表没法画了，限制在10个结果
        result = stats_word.stats_word(content,10)
        #由于typing.Counter输出的结果是一个奇怪的列表
        #形式如：[('a',8),('b',2)...]，所以必须用numpy来处理
        np_list=np.array(result) #将文本处理结果转化为二维数组
        word_list=[] #初始化盛放词的列表
        number_list=[] #初始化盛放词频的列表
        for i in range(len(np_list)): #拆分Numpy多维数组
            word_list+=[np_list[i][0]]
            #Numpy在处理('a',8)的时候，会把8记录为'8'，所以需要强制转换类型为int
            number_list+=[int(np_list[i][1])]
        
    
        plt.rcdefaults()
        
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        fig, ax = plt.subplots()
        y_pos = np.arange(len(word_list))

        ax.barh(y_pos, number_list, align='center', color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(word_list)
        ax.invert_yaxis()
        ax.set_xlabel('词频')
        ax.set_title('好友分享文章词频统计')
        plt.savefig("stats.png") #保存图片
        msg.reply_image("stats.png") #回复图片

    embed() #堵塞线程，保持监听状态

if __name__ == '__main__':
    main()