# day12
from os import path
from wxpy import *
import requests
import getpass
from pyquery import PyQuery
from mymodule import stats_word
import matplotlib.pyplot as plt
import numpy as np


# 获取当前工作目录
cwd = path.abspath(path.dirname(__file__))
# 设置中文字体(因为matplotlib默认不支持中文字体)
import matplotlib
plt.rcParams['font.family'] = ['Arial Unicode MS']


# 提取微信公众号文章正文
def get_article(url):
    r = requests.get(url)
    document = PyQuery(r.text)
    return document('#js_content').text()


# 生成图片
def generate_image(data, image_path):
    labels = [v[0] for v in data]   # 获得每个元组里的第一个值
    widths = [v[1] for v in data]   # 获得第二个值（出现的次数）作为x轴的值
    ypos = range(len(data))  # 获取y轴有多少元素，就生成多少行
    fig, ax = plt.subplots()  # 初始化一个图标
    ax.barh(ypos, widths)  # ax就是生成的坐标系
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  # 默认是从小到大的so这里invert一下
    ax.set_ylabel('关键字')
    ax.set_xlabel('词频')
    ax.set_title('词频统计')
    fig.savefig(image_path, bbox_inches='tight')


def main(): 
    bot = Bot() #登录微信的命令
    my_friends = bot.friends().search('大头鬼啊')  #搜索名称含有“大头鬼啊-”的好友。bot.friends()→发送给所有好友
#监听好友消息
#通过装饰器，注册一个接收制定好友分享消息的函数
    @bot.register(my_friends, SHARING)
    def friend_sharing(msg):
    # 使用requests获得网络链接的文本
        article = get_article(msg.url)
        result = stats_word.stats_text_cn(article, 10)
        image_path = path.join(cwd, 'stats.png')
        generate_image(result, image_path)
        msg.reply_image(image_path)
# 让程序保持运行。如果不加这一句，程序运行完就会退出。
    embed() 


def test():
    article = get_article('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    result = stats_word.stats_text_cn(article, 10)
    image_path = path.join(cwd, 'stats.png')
    generate_image(result, image_path)

if __name__ == "__main__":
    # main()
    test()


