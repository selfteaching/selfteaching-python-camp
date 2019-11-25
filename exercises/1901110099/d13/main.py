from os import path
cwd = path.abspath(path.dirname(__file__)) #获取当前工作目录

import matplotlib.pyplot as plt 
plt.rcParams['font.sans-serif'] = 'simHei' #设置中文字体
#plt.rcParams['font.sans-serif'] =["KaiTi"] #中文乱码的处理
#plt.rcParams['axes.unicode_minus'] = False

# 提取微信公众号文章正文
import requests #使用 requests 请求文章的链接，获取返回结果
import pyquery
from pyquery import PyQuery #提取微信正⽂
def get_article(url):
    r = requests.get(url)   
    document = PyQuery(r.text)
    return document('#js_content').text()


# 生成图片
import numpy as np
def generate_image(data, image_path):    
    labels = [v[0] for v in data]   
    widths = [v[1] for v in data]
    ypos = range(len(data))  #获取y轴有多少元素，就生成多少行
    fig, ax = plt.subplots()  #初始化一个图标
    ax.barh(ypos, widths)  #ax就是生成的坐标系
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels) #设置 y 轴的标签名称
    ax.invert_yaxis() #反转 y 轴
    ax.set_ylabel('关键字') 
    ax.set_xlabel('词频')
    ax.set_title('词频统计')
    fig.savefig(image_path, bbox_inches='tight')
    plt.show() #显示此图表

from wxpy import *
from mymodule import stats_word
import logging
def main():
    bot = Bot() #初始化机器人，扫码登陆
    friends = bot.friends() #找到所有好友

    @bot.register(friends,SHARING) #监听好友信息，自动响应分享类型的消息

    def handler(msg):
        try:
            article = get_article(msg.url)
            result = str(stats_word.stats_text(article,100))
            logging.info('sharing url = %s',msg.url)
            image_path = path.join(cwd, 'stats.png')
            generate_image(result, image_path)
            msg.reply_image(image_path)
        except Exception as e:
            logging.exception(e)
    embed() #进入 Python 命令行、让程序保持运行

def test():
    article = get_article('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    result = stats_word.stats_text(article,20)
    image_path = path.join(cwd, 'stats.png')
    generate_image(result, image_path)

if __name__ == "__main__":
    test()
    #main()








