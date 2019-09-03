'''Day13任务：将微信好友文章中的词频最高前20个词的结果以图表返回给好友'''
# Matplotlib 可能是 Python 2D-绘图领域使用最广泛的套件, 它能让使用者很轻松地将数据图形化，并且提供多样化的输出格式。

import requests
import pyquery      
from mymodule.stats_word import stats_text     # 从 模块中(mymodule是包，stats_word是模块) 导入 函数stats_text
import matplotlib.pyplot as plt                 # 导入matplotlib模块
import numpy as np                             # 导入numpy模块
import os 

# 第一步：引入wxpy模块，监听好友消息，获取SHARING类型消息的网页链接
import wxpy                                   # 导入wxpy模块，由于Bot,SHARING,embed是wxpy模块下的，所以他们三个前面都加上wxpy。如果用from wxpy import *，则不需要添加。
bot = wxpy.Bot()                              # 初始化机器人，会出现一个二维码，扫码登录即可
my_friend = bot.friends().search('熊小腰')[0]  # 搜索名字含有“熊小腰”的朋友(如果针对所有好友，可以用friends=bot.friends())
# my_friend = bot.friends()
@bot.register(my_friend, wxpy.SHARING)        # 接受好友类型为sharing的消息。这个是装饰器，装饰它下面的函数。其中，指定了my_friend和消息类型。如果是所有好友，则是@bot.register(friends,SHARING)
def receive_mf(msg):                          # 参数msg为监听到的微信好友消息 
    r = requests.get(msg.url)                 # 请求sharing类型消息的网页链接msg.url
    
# 第二步：将获取的链接用Day11项目中的代码进行处理，调用函数进行词频统计
    document = pyquery.PyQuery(r.text)            # 通过pyquery解析该网页
    content = document('#js_content').text()      # '#js_content'是网页的一个标签名，这个标签中存放着文档的内容。
    text=content                                  # 将content赋值给text
    result = stats_text(text,20)                 # 结果result是Counter对象（dict的子类）的key是待计数元素，value是对应的计数
    print(result)
    
# 第三步：将结果生成一张图表文件
    np.random.seed(19680801)     # fixing random state for reproducibility
    plt.rcdefaults()             # 从Matplotlib的内部默认样式恢复rc参数
    fig,ax = plt.subplots()      # 创建一个图形和一组子图
    # process data
    word_list = [x[0] for x in result]               # 将Counter对象的key赋值给列表，元素即为中文词语
    frequency_list = [x[1] for x in result]          # 将Counter对象的value赋值给列表,元素即为词频
    y_pos = np.arange(len(word_list))                # 纵轴设置，在给定间隔内返回均匀间隔的值
    error = np.random.rand(len(word_list))

    from pylab import mpl                            # 在python脚本中动态设置matplotlibrc
    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False      # 解决保存图像是负号'-'显示为方块的问题

    ax.barh(y_pos, frequency_list, xerr=error, align='center', color='gyb') # 颜色为绿、黄、蓝
    ax.set_yticks(y_pos)
    ax.set_yticklabels(word_list)
    ax.invert_yaxis()                                # labels read top-to-bottom
    ax.set_xlabel('词频')
    ax.set_title('top20词频的统计图')
    # plt.show()                                       # 屏幕上显示柱状图，在我的电脑上，这行代码必须要注释掉，否则返回不了图表结果
    
    img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'wx.png')   # 指定文件的保存路径
    
# 第四步：把图表文件发送给微信好友
    # plt.savefig('day13.png')                         # 保存图表文件
    # msg.reply_image('day13.png')                    # my_friend.send_image('day13.png') 用不了 

    plt.savefig(img_path)                         # 保存图表文件
    msg.reply_image(img_path)

wxpy.embed()             # 进入Python命令行，让程序保持运行

# 笔记
# 第49行 为什么my_friend.send_image('day13.png') 用不了?
# 现在使用@bot.register()，如果朋友有消息过来是会接收到，相当于打开了一个聊天窗口，或相当于接通了电话线，使用msg.reply就相当于直接说话。
# 如果直接使用myfriend.send，则是要在上面这个窗口之外使用，相当于将当前窗口关闭另开一个窗口，或者另拨通电话。