# 监听好友消息,获取消息网页链接
# 把获取到的连接使用DAY11作业去分析,
# 把结果返回给对应好友
from wxpy import *
import requests                         #输入requests网络请求库
import yagmail
import getpass
from pyquery import PyQuery as py
import stats_word13 as sw
import matplotlib.pyplot as plt
import numpy as np
import jieba
#matplotlib显示中文方法
plt.rcdefaults()                            #从最初由Matplotlib加载的rc文件中恢复rc参数。
plt.rcParams['font.sans-serif']=['SimHei']  #用来正常显示中文标签，SimHei代表：黑体。
plt.rcParams['axes.unicode_minus']=False    #用来正常显示负号

bot =Bot()#扫码登录
bot.enable_puid()

# 自动响应各种信息
@bot.register()
def print_others(msg):
    print(msg)

my_friend =bot.friends()#获取所有好友


@bot.register(my_friend,SHARING)   ##将 Bot.register() 作为函数的装饰器，即可完成注册。监听好友消息，如果好友的消息为分享型的，则获取消息的网页连接（msg.url)
def auto_reply_sharing_msg(msg):
    print("收到的新消息：",msg)
    url=msg.url   #其中的raw是原始数据的意思
    print("对应的url",url)
    need_reply_friend=msg.sender#文件的发送者
    print("需要回应的朋友",need_reply_friend)

    r = requests.get(url)#获取网页数据 
    web_text =r.text     #使用变量web_text保护网页文本数据(这时会保存很多js代码以及其他function的代码,并不是里面所有的东西是我们需要的)
    document=py(web_text)
    content =document('#js_content').text()#js_content 是网页主文内容的div ,id为js_content,以后我们爬不同的数据,需要去看一下别人家的网页代码

    print("content",content)#测试看一下得回来的数据是什么
    result = sw.stats_text_cn(content,20)
    result_list =list(result)        #弄成表的形式
    print("reusult_list",result_list)

    need_reply_friend.send_msg(result_list)

    #返回结果处理部分
    x_ax=[]
    y_ax=[]
    for item in result:
        x_ax.append(item[0])
        y_ax.append(item[1])

    #图表部分
    fig, ax = plt.subplots()
    fig, ax = plt.subplots()

    # Example data

    y_pos = np.arange(len(x_ax))

    performance = y_ax

    error = np.random.rand(len(x_ax))

    ax.barh(y_pos, performance, xerr=error, align='center',

            color='green', ecolor='black')

    ax.set_yticks(y_pos)

    ax.set_yticklabels(x_ax)

    ax.invert_yaxis()  # labels read top-to-bottom

    ax.set_xlabel('字符')

    ax.set_title('所发文章的词频')

    plt.savefig("examples.jpg")

    need_reply_friend.send_image('examples.jpg')

    plt.show()

embed()    # 堵塞线程，并进入 Python 命令行

'''
    need_reply_friend.send_msg(result)

    #返回结果处理部分
    x_ax=[]
    y_ax=[]
embed()    # 堵塞线程，并进入 Python 命令行

'''