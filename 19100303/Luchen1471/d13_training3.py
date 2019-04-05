#把d11练习里面的功能，先定义一个函数出来
import requests
from mymodule import stats_word
from pyquery import PyQuery

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def dealwiththemsg(msg0):    
    response = requests.get(msg0.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    str_con = str(content)
    #return str(stats_word.stats_text_cn(str_con))
    #print(str(stats_word.stats_text_cn(str_con)))
    data_list = stats_word.stats_text_cn(str_con)
    #列表换字典，但是i[0]和i[1]是什么意思没明白
    data_dic = {}
    for i in data_list:
        data_dic[i[0]] = i[1]
    #下面开始画图
    #https://matplotlib.org/tutorials/introductory/lifecycle.html#sphx-glr-tutorials-introductory-lifecycle-py
    group_data = list(data_dic.values())
    group_names = list(data_dic.keys())
    group_mean = np.mean(group_data)
    fig, ax = plt.subplots()
    plt.rcParams['font.sans-serif']=['SimHei']#改中文字体
    ax.barh(group_names, group_data)
    #print(plt.style.available)
    #plt.style.use('fivethirtyeight')
    #print(type(ax.barh(group_names, group_data)))
    plt.savefig('my_result.png')  # 保存为图片
    #msg.reply_image('my_result.png') 
    return 'my_result.png'


from wxpy import *
bot = Bot(login_callback= True) #对回调并不理解

#Bot.enable_puid(path='wxpy_puid.pkl') #不用puid绑定也没问题吧
my_friend = bot.friends().search('小圆来了',sex=FEMALE)[0]
my_friend.send('你把文章转发给我（自动发送）') 
#bot.file_helper.send('Hello from wxpy!')

@bot.register(my_friend,SHARING)                   #再看官方文件
def friend_sharing(msg):
    msg.reply_image(dealwiththemsg(msg))                 #给好友发送内容
    

embed()

