import requests
from pyquery import PyQuery
import stats_word
import matplotlib.pyplot as plt 
import numpy as np 
from wxpy import *

bot = Bot()
my_friend = bot.friends().search('')[0]
my_friend.send('程序测试，请给我发送一篇文章')

@bot.register(my_friend)
def return_msg(msg):
    if msg.type == 'Sharing':
        r = requests.get(msg.url)
        document = PyQuery(r.text)
        content = document('#js_content').text()
        r_list = stats_word.stats_text(content,10)
        r_dic = dict(r_list)
        keys,values = zip(*r_dic.items())

        plt.rcdefaults()
        fig, ax = plt.subplots()

        people = r_list
        y_pos = np.arange(len(people))
        error = np.random.rand(len(people))
        word_frequency = values

        plt.rcParams['font.sans_self']=['SimHei']
        ax.barh(y_pos, word_frequency,xerr=error,align='center',color='green',ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(keys)
        ax.invert_yaxis()
        ax.set_xlabel('次数')
        ax.set_title('文章词频统计如下')
        
        plt.savefig('d13.png')
        msg.reply_image('d13.png')
embed()      