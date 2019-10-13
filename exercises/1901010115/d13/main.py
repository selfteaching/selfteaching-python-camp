from mymodule import stats_word #读取模块
import json #引入jsan解码库
import jieba

import requests #引入requests库用于获取网页HTML信息

import pandas
import numpy as np
import matplotlib.pyplot as plt

from pyquery import PyQuery as pq #引入pyquery库解析获取的HTML信息

from wxpy import * #引入wxpy模块
bot = Bot(cache_path=True) #初始化wxpy，扫码登录
my_friend = bot.friends() #搜索好友信息
@bot.register(my_friend,SHARING) #注册消息接收器（并限定为来自好友的，分享类信息）
def my_friend_sharing(msg): #定义函数 ，当有msg发送过来，则用requests模块获取该网址
    msg_sharing = requests.get('msg.url') #这里就是获取msg的网址信息了
    doc = pq(msg_sharing.text) #解析HTML代码
    msg_content = doc('#js_content').text() #提取文本
    msg_result = stats_word.cn(msg_content,10) #引用模块统计处理文本
    
    plt.rcdefaults() #固定语法，啥意思？？？
    fig,ax = plt.subplots() #固定语法，引入图层？？？
    plt.rcParams['font.sans-serif']=['SimHei'] #引入汉字输入功能
    dict_result = dict(msg_result) #字典化了那个统计结果列表，应该直接可转吧
    x_val = [] #空列表
    y_val = [] #空列表
    for keys,values in dict_result: #分别提取统计结果的键和数量值
        x_val.append(keys)
        y_val.append(values)
    y_pos = np.arange(len(x_val)) #y轴的范围设定为0到xv的个数？？？
    error = np.random.rand(len(x_val)) #啥意思？？？
        
    ax.barh(y_pos,y_val,xerr=error,align='center') #设置一个y轴为y_pos,x轴为y_val的条形图，xerr不知控制什么，align为设定子图居于有值的视窗中间
    ax.set_yticks(y_pos) #设定y轴上的值个数，本案例为10
    ax.set_yticklabels(x_val) #y轴上各个节点的标签设定为x_val内的数据，本案例即排在前10的10个汉字
    ax.invert_yaxis() #标签由上至下读取？？？
    ax.set_xlabel('高频汉字') #设置y轴的标题
    ax.set_ylabel('出现次数') #设置x轴的标题
    ax.set_title('词频统计表') #设置图形的标题
    plt.savefig("词频统计图.png") #应该是把该图另存为“词频统计图。png”，这个在刚才的网搜没搜到
    
    msg.reply_image("词频统计图.png") #12节wxpy模块的运用，记不太清了，见过

#以上函数没有使用return等结构我没太看懂，应该是@装饰器的使用与一般的函数不一样，得查询清楚
embed() #堵塞线程。确保Terminal在运行完以上函数后，仍能在线接受新信息



#本次作业由于微信改版的原因，wxpy库不能正常运行，一直报错'pass ticket'。所以以上代码是未经测试的，回头阅读完装饰器内容后，找机会回来做测试。