from wxpy import *
import requests
from pyquery import PyQuery
import stats_word
import matplotlib.pyplot as plt
import numpy as np

bot = Bot()
my_friend=bot.friends().search("彤姐")[0]
my_friend.send("hi，此条信息为机器人自动推送~")
@bot.register(my_friend,SHARING)
def my_friend_sharing(msg):
    msg=msg.url
    r = requests.get(msg)
    document=PyQuery(r.text)
    content = document('#js_content').text()
    a=stats_word.stats_text(content,10)
    b=dict(a)
    keys,values=zip(*b.items())


    plt.rcdefaults()#从Matplotlib的内部默认样式恢复rc参数
    fig, ax = plt.subplots()#创建一个图形和一组子图

    word=a
    y_pos = np.arange(len(word))#在给定间隔内返回均匀间隔的值。
    performance = 3 + 10 * np.random.rand(len(word))#给定形状的随机值。
    error = np.random.rand(len(word))
    
    plt.rcParams['font.sans-serif']=['SimHei'] #不用这行会出现中文字变框框，windows平台可用
    
    
    ax.barh(y_pos, values, xerr=error, align='center',color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(keys)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('词频数目')
    ax.set_title('统计词频图表')

    plt.savefig("day13.png")
    my_friend.send_image("day13.png")

embed()