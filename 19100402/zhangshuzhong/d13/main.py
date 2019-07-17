import requests
import pyquery
import yagmail
import getpass
from mymodule import stats_word
from pyquery import PyQuery
import numpy as np
import matplotlib.pyplot as plt

#导入模块
from wxpy import *
#初始化机器人，扫码登录
bot = Bot()
#搜索名称含有“张书忠”的好友
my_friends=bot.friends().search('张书忠')[0]
#给好友发送信息
#my_friends.send('你好')


#监听好友消息
#通过装饰器，注册一个接收制定好友分享消息的函数
@bot.register(my_friends,SHARING)
def friend_sharing(msg):
    #获得分享内容的网络链接
    dizhi=msg.url
    #使用requests获得获得网络链接的文本
    response = requests.get(dizhi)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    #将获得的文章进行分词
    text = stats_word.stats_text_cn(content,20)
    #将上面的结果是一个列表，现将其转化为字典，以便提取坐标轴的变量
    text1={}
    for i in text:
        text1[i[0]] = i[1]
        #这时text2就是一个包含词于词频的字典
        # #下面设置坐标轴中x轴与y轴的数值
    y=tuple(text1.keys())
    x=tuple(text1.values())
    #显示中文为黑体
    plt.rc('font', family='SimHei', size=12)
    #建立一个子图像对象
    fig,ax=plt.subplots()
    #生成一个水平的条形图
    ax.barh(y, x,align='center', color='blue', ecolor='black')
    #设置y轴的刻度字体大小
    plt.yticks(fontsize=8)
    
    #反转y轴
    ax.invert_yaxis() 
    
    #设置x轴的标签名称
    ax.set_xlabel('统计词语的词频')
    #整个图的标题
    ax.set_title('从分享的文章中统计的词语词频前20的词')
    
    #显示柱状图，并将图保存为名字为“tongji”的jpg格式图片
    plt.savefig("tongji.jpg")
    
    #给好友发送图片
    my_friends.send_image('tongji.jpg')
#让程序保持运行
embed()