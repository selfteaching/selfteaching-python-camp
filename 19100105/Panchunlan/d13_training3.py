import requests
from mymodule import stats_word
from pyquery import PyQuery
# 导入模块
from wxpy import *
bot = Bot(console_qr=2,cache_path="botoo.pkl")



# 搜索名称含有 "高" 的男性江苏好友
my_friend = bot.friends().search('朱高')[0]


# 发送文本给好友
my_friend.send('请给我转发一篇文章，谢谢！')

# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(my_friend)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

    if msg.type == 'sharing':
        print(msg)
        response = requests.get('msg.url')   #请求获得内容

        document = PyQuery(response.text)
        content = document('#js_content').text()
        print(content)
        result = str(stats_word.stats_text(content))
        my_friend.send(result)
        
import matplotlib.pyplot as plt
import numpy as np


def Horizontal_bar_chart(data):
    '''修复随机状态'''
    np.random.seed(19680801)

    '''不知道在干什么，好像是定义变量'''
    plt.rcdefaults()
    fig, ax = plt.subplots()

    '''处理数据'''
    words = (data[0])
    y_pos = np.arange(len(words))
    number = 3 + 10* np.random.rand(len(words))
    error = np.random.rand(len(words))

    '''设置图表样式'''
    ax.barh(y_pos,number,xerr = error,align = 'center',color = 'bule',ecolor = 'black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(words)
    ax.invert_yaxis()
    ax.set_xlabel('出现次数')
    ax.set_title('关于您发给我分享文章中的中文词频统计图表')
    
   

 #plt.show()

plt.savefig("C:/Users/Administrator/Panchunlan.png")

embed()
