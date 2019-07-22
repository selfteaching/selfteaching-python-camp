from wxpy import *
import stats_word
import requests
from pyquery import PyQuery
from matplotlib.font_manager import FontProperties
import numpy as np
import matplotlib.pyplot as plt

def main():
    # 初始化机器人，扫码登陆
    bot = Bot()
    # 搜索好友
    my_friend = bot.friends()
    # 回复 my_friend 的消息 (优先匹配后注册的函数!)
    @bot.register(my_friend,SHARING)
    
    def auto_accept_friends(msg):
        response = requests.get(msg.url) 
        document = PyQuery(response.text)
        content = document('#js_content').text()
        result = stats_word.stats_text_cn(content)

        np_list=np.array(result) #将文本处理结果转化为二维数组
        word_list=[] #初始化盛放词的列表
        number_list=[] #初始化盛放词频的列表
        for i in range(len(np_list)): #拆分Numpy多维数组
            word_list+=[np_list[i][0]]
            #Numpy在处理('a',8)的时候，会把8记录为'8'，所以需要强制转换类型为int
            number_list+=[int(np_list[i][1])]
        font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=8)
        plt.rcdefaults()
        ax = plt.subplots()
        y_pos = np.arange(len(word_list))
        ax.barh(y_pos, number_list, align='center', color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(word_list, fontproperties=font)
        ax.invert_yaxis()
        ax.set_xlabel('词频', fontproperties=font)
        ax.set_title('好友分享文章词频统计', fontproperties=font)
        plt.savefig("stats.png") #保存图片
        msg.reply_image("stats.png") #回复图片
    
    # 进入 Python 命令行、让程序保持运行
    embed()
if __name__ == '__main__':
    main()