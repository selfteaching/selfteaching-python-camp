#coding:utf-8
from pyquery import PyQuery
from wxpy import *
import requests
import getpass
import mymodule.stats_word
import matplotlib.pyplot as plt
from matplotlib.font_manager import *

import matplotlib
matplotlib.matplotlib_fname() #将会获得matplotlib包所在文件夹
import numpy as np

pic_path = 'C:\\Users\\flami\Documents\\GitHub\\selfteaching-python-camp\\19100303\\lunbixiaozi\\'

###pictures:

def pic_create(counter_cn_dict):
    counter_cn_dict_keys = []
    counter_cn_dict_values = []
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    myfont = FontProperties(fname='C:/ProgramData/Anaconda3/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf')
    plt.rcdefaults()
    fig, ax = plt.subplots()

    for i in counter_cn_dict.keys(): 
        counter_cn_dict_keys.append(i)
    for i in counter_cn_dict.values(): 
        counter_cn_dict_values.append(i)



    y_pos = np.arange(len(counter_cn_dict_keys))

    ax.barh(y_pos, counter_cn_dict_values, align='center', color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(counter_cn_dict_keys, fontproperties=myfont)
    ax.invert_yaxis()
    ax.set_xlabel('Counts')
    ax.set_title('词频统计', fontproperties=myfont)
    plt.savefig(pic_path + 'frequency.jpg')
    #plt.show()

if __name__=="__main__":
    bot = Bot()
    myself = bot.self
    bot.file_helper.send('Hello from wxpy!')
    @bot.register()
    def print_messages(msg):
        if msg.type == SHARING:
            r=requests.get(msg.url,auth=('user','pass')) 
            document=PyQuery(r.text)
            content=document('#js_content').text()
            counter_cn_dict = mymodule.stats_word.stats_text_cn(content, 20)
            pic_create(counter_cn_dict)
    
            msg.reply_image(pic_path + 'frequency.jpg' )
        
    embed()
    