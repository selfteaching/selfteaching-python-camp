# 19100304 day13 银零
# 1.在 d12_training2.py 的基础上进行更新，将其中的结果生成一张图表图片文件



import requests
import pyquery
from pyquery import PyQuery
from mymodule import stats_word
from wxpy import *

import matplotlib.pyplot as plt
import numpy as np


bot = Bot()
my_friend = bot.friends().search('银零',sex = MALE, city = '上海')[0]

@bot.register(my_friend)
def reply_my_friend(msg):
    if msg.type =='Sharing':
        response = requests.get(msg.url)   
        document = PyQuery(response.text)    
        content = document('#js_content').text()
        list_content = stats_word.stats_text(content,100)
        dict_content = dict(list_content)
        def chartImg(data=dict_content) :
            group_x = list(data.values())
            group_y = list(data.keys())
            fig, ax = plt.subplots()
            plt.title('词频统计表',color='black',fontproperties = cnfont,fontsize = 16)
            ax.set_xlabel('词频',fontproperties = cnfont, color = 'grey')
            ax.set_ylabel('词组',fontproperties = cnfont, color = 'grey')
            ax.set_yticklabels(group_y,fontproperties = cnfont)
            ax.barh(group_y,group_x)
            plt.savefig('chart.png')
        return 'chart.png'
    else:
        pass
embed()




