import requests
import pyquery
from pyquery import PyQuery
import stats_word
import matplotlib.pyplot as plt
import numpy as np
from wxpy import * #  导入微信机器人模块

bot = Bot() #初始化机器人，扫码登录
my_friend = bot.friends().search('xx', sex=MALE, city="xx")[0] #测试
my_friend.send('请给我发送一篇文章')

@bot.register(my_friend)
def return_msg(msg):
    if msg.type == 'Sharing': #sharing 分享的公众号文章
        r = requests.get(msg.url) #解析获取公众号文章的url
        document = PyQuery(r.text)
        content = document('#js_content').text()
        r_list = stats_word.stats_text(content,10)
        r_dic = dict(r_list) #字典化
        keys,values = zip(*r_dic.items()) #拆分单词和统计字数
        
        plt.rcdefaults()
        fig, ax = plt.subplots()
        
        # Example data
        people = r_list
        y_pos = np.arange(len(people))
        performance = 3 + 10 * np.random.rand(len(people))
        error = np.random.rand(len(people))
        word_frequency = values

        plt.rcParams['font.sans-serif']=['SimHei'] #不用这行会出现中文字变框框，windows平台可用
        ax.barh(y_pos, word_frequency, xerr=error, align='center',color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(keys)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('次数')
        ax.set_title('文章高频词统计如下')
        
        plt.savefig('day13.png')
        msg.reply_image('day13.png')
embed()

        