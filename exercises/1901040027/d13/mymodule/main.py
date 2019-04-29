
import requests
import pyquery
from pyquery import PyQuery
import stats_word
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np

#初始化机器人，扫码登陆
bot = Bot()
#找到好友
my_friend = bot.friends().search('小企鹅1')[0]
#发送文本给好友
my_friend.send('程序测试，转发任意微信推文给我，完成测试')
#监听消息
@bot.register()
def print_others(msg):
        print(msg)


#回复my_friend的消息
@bot.register(my_friend)
def reply_my_friend(msg):
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()

        r_list = stats_word.stats_text_cn(content,10)
        #return r_list
        r_dic = dict(r_list)
        keys, values = zip(*r_dic.items())# 拆分单词和统计数字


#引入matplotlib和numpy
        plt.rcdefaults()
        fig, ax = plt.subplots()

        people = r_list
        y_pos = np.arange(len(people))
        performance = 3 + 10 * np.random.rand(len(people))
        error = np.random.rand(len(people))
        word_frequency = values

        #from matplotlib.font_manager import FontProperties
        #font = FontProperties(fname='/Library/Fonts/Songti.ttc')

        #plt.rcParams['font.sans-serif']=['Songti']#统计表格数据格式汉化
        plt.rcParams['font.sans-serif']=['SimHei']#统计表格数据格式汉化

        ax.barh(y_pos, word_frequency, xerr = error, align = 'center', color = 'green', ecolor = 'black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(keys) #设置Y轴内容
        ax.invert_yaxis() #labels read top-to-bottom
        ax.set_xlabel('词频数') #设置x轴内容
        ax.set_title('好友分享文章词频统计')

        plt.savefig('data.png')
        msg.reply_image('data.png')


embed() #保持监听


