# 导入模块
import matplotlib.pyplot as plt
import numpy as np
from wxpy import * 
import requests
from pyquery import PyQuery
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

#统计图表
def stats_plt(a):
    
    np.random.seed(19680801) # Fixing random state for reproducibility


    plt.rcdefaults()
    fig, ax = plt.subplots()

     # Example data
    people = (a)
    y_pos = np.arange(len(a)) #Y轴数据名称
    performance = 3 + 10 * np.random.rand(len(a)) #Y轴数据
    error = np.random.rand(len(a)) 
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常现实中文标签

    ax.barh(y_pos, performance, xerr=error, align='center',
        color='red', ecolor='yellow') #数据加载方式
    ax.set_yticks(y_pos)
    ax.set_yticklabels(a) #设置Y轴名称
    ax.invert_yaxis()  # labels read top-to-bottom 反转Y轴方向
    ax.set_xlabel('Performance') 
    ax.set_title('speak in public')#标题


    plt.show()
    return plt.show


# 初始化机器人，扫码登陆

bot = Bot()

# 搜索名称含有 " " 的好友
my_friend = bot.friends()

# 发送文本给好友
#my_friend.send('Hello WeChat!')

# 发送图片
#my_friend.send_image('my_picture.jpg')

#
@bot.register([Groups,Friend], SHARING, except_self = False)
#def word_frequency(meg) :
def print_others(msg):
    print(msg)
    response = requests.get(msg.url) #提取公众号伪代码
    document = PyQuery(response.text)
    content = document('#js_content').text() #把抓取的内容写成可视的文字
    #print(content) 节点测试
    import  mymodule.stats_word
    #统计内容的前100词频
    statlist = mymodule.stats_word.stats_text_cn(content,6)
    statString = "".join(str(i) for i in statlist)
    stats_plt(statString)
    msg.reply_image(statString)
    #return statString

    #print(statlist) 节点测试
embed()# 进入 Python 命令行、让程序保持行




    