import requests  # 网络请求库
from pyquery import PyQuery  # 文档解析库
from stats_word import stats_text_cn  # 统计中文词频
from wxpy import *  # 导入微信机器人模块
import matplotlib.pyplot as plt  # 可视化操作界面
import numpy as np   # 数值数学扩展包


bot = Bot(cache_path=True) # 初始化机器人，扫码登陆

my_friend = bot.friends() # 所有好友

@bot.register(my_friend,SHARING) # 消息接收监听器，获取分享类型的消息

def print_friend_messages(msg):
    response = requests.get(msg.url)    # 发送请求,url对应的页面内容
    document = PyQuery(response.text)     # 传入HTML代码
    content = document('#js_content').text()

    count = 50 # 统计50个中文词汇
    r_list = stats_text_cn(content,count)   # 统计前50个中文词频
    r_dict = dict(r_list)  # 转换成dict类型

    plt.rcdefaults()    # 重置rc所有的默认参数
    fig, ax = plt.subplots()    # 返回一个figure图像和子图ax的array列表 

    plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签  
    plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

    counter_list = sorted(r_dict.items(), key=lambda x: x[1], reverse=True)
    label = list(map(lambda x: x[0], counter_list[:20]))
    value = list(map(lambda y: y[1], counter_list[:20]))

    # 水平直方图
    ax.barh(range(len(value)), value, tick_label=label, align='center',  color='green')     

    ax.invert_yaxis()  # labels read top-to-bottom，Y轴可逆显示
    ax.set_xlabel('词频数',fontsize=12)    # X轴标签
    ax.set_ylabel('中文词汇',fontsize=12)    # Y轴标签
    ax.set_title('文章中前20的词频统计图',fontsize=16)    # 标题
    
    plt.savefig('stats.png')    # 保存图片
   
    msg.reply_image('stats.png')  # 给好友回复图片
    #plt.show()  
        

embed() # 进入Python命令行，让程序保持运行


