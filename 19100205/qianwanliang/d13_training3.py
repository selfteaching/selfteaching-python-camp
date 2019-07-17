# 用系统的中文字体
from pylab import * 
import matplotlib
matplotlib.rcParams['font.family'] = 'YaHei Monaco Hybird'
mpl.rcParams['font.sans-serif'] = ['YaHei Monaco Hybird'] #更新字体格式
mpl.rcParams['font.size'] = 9

import sys
import matplotlib.pyplot as plt
import numpy as  np
from wxpy import *
from pyquery import PyQuery
import requests
import mymodule.stats_word

bot = Bot()
my_friend = bot.friends().search('阳')[0]
my_friend.send('hi')

@bot.register()
def get_msg (msg) :
    if msg.type == 'Sharing':
        response = requests.get(msg.url)
        document = PyQuery(response.text) 
        #rint(document) #调试用
        content = document('#js_content').text()
        #print(content) #调试用
      
        result = mymodule.stats_word.stats_text_cn(content, 20)
        #print(result) # 调试用
        convert_result_to_str = ''.join(str(i) for i in result)
        print(convert_result_to_str)

        cizu=[]
        for i in range(0,20):
            cizu.append(result[i][0])
        # print(cizu) #调试用

        cipin=[]
        for i in range(0,20):
            cipin.append(result[i][1])
        #print(cipin) #调试用

        y_pos = np.arange(len(cizu))
        fig, ax = plt.subplots()
        ax.barh(y_pos, cipin, align='center',color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(cizu)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_ylabel('词组')
        ax.set_xlabel('词频')
        ax.set_title('词频统计')
        plt.savefig("C:/TEMP/cipin_for_PYcamp_day13.png") # 中转&结果留存
        msg.sender.send_image("C:/TEMP/cipin_for_PYcamp_day13.png")
        plt.show() #调试用
        #print(msg.sender)msg.sender.send(result)
        #msg.sender.send_image("baishanheishui.png")


    else :
        pass
embed()# 用系统的中文字体
from pylab import * 
import matplotlib
matplotlib.rcParams['font.family'] = 'YaHei Monaco Hybird'
mpl.rcParams['font.sans-serif'] = ['YaHei Monaco Hybird'] #更新字体格式
mpl.rcParams['font.size'] = 9

import sys
import matplotlib.pyplot as plt
import numpy as  np
from wxpy import *
from pyquery import PyQuery
import requests
import mymodule.stats_word

bot = Bot()
my_friend = bot.friends().search('风雨同舟')[0]
my_friend.send('hi')

@bot.register()
def get_msg (msg) :
    if msg.type == 'Sharing':
        response = requests.get(msg.url)
        document = PyQuery(response.text) 
        #rint(document) #调试用
        content = document('#js_content').text()
        #print(content) #调试用
      
        result = mymodule.stats_word.stats_text_cn(content, 20)
        #print(result) # 调试用
        convert_result_to_str = ''.join(str(i) for i in result)
        print(convert_result_to_str)

        cizu=[]
        for i in range(0,20):
            cizu.append(result[i][0])
        # print(cizu) #调试用

        cipin=[]
        for i in range(0,20):
            cipin.append(result[i][1])
        #print(cipin) #调试用

        y_pos = np.arange(len(cizu))
        fig, ax = plt.subplots()
        ax.barh(y_pos, cipin, align='center',color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(cizu)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_ylabel('词组')
        ax.set_xlabel('词频')
        ax.set_title('词频统计')
        plt.savefig("C:/TEMP/cipin_for_PYcamp_day13.png") # 中转&结果留存
        msg.sender.send_image("C:/TEMP/cipin_for_PYcamp_day13.png")
        plt.show() #调试用
        #print(msg.sender)msg.sender.send(result)
        #msg.sender.send_image("baishanheishui.png")


    else :
        pass
embed()