

from stats_word import stats_text_cn
import requests
from pyquery import PyQuery
import logging
import getpass
from os import path
import matplotlib.pyplot as plt
import numpy as np
from wxpy import *

cwd = path.abspath(path.dirname(__file__))  #获取当前工作目录
plt.rcParams["font.sans-serif"] = "SimHei"  #设置中文字体

logging.basicConfig(format="file:%(filename)s|line:%(lineno)d|message:%(message)s",level=logging.DEBUG) #初始化logging模块

def get_article(url):    #获取微信分享文章的正文内容
    response = requests.get(url)
    document = PyQuery(response.text)
    return document("#js_content").text()

def generate_image(data,image_path):    #生成图片
    labels = [v[0] for v in data]
    width = [v[1] for v in data]
    ypos = range(len(data))
    fig, ax = plt.subplots()
    ax.barh(ypos,width)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel("使用频率")
    ax.set_ylabel("词语")
    ax.set_title("此文章使用最多的20个词语")
    fig.savefig(image_path,bbox_inches="tight")

def main():                                  #初始化机器人，扫码登录
    bot = Bot()
    my_friend = bot.friends()
    @bot.register(chats=my_friend,msg_types=SHARING,except_self=True,run_async=True,enabled=True)
    def handler(msg):                               #回复统计结果图
        try:
            article = get_article(msg.url)
            logging.info("sharing url = %s",msg,url)
            data = stats_text_cn(article,20)
            image_path = path.join(cwd, "Analyse.jpg")
            generate_image(data,image_path)
            msg.reply_image(image_path)
        except Exception as e:
            logging.exception(e)
    embed()

def test():                                    #进行测试
    article = get_article("https://mp.weixin.qq.com/s/HGpeha9R3XwFPlL5wCy6xA")
    data = stats_text_cn(article,20)
    image_path = path.join(cwd, "Analyse.jpg")
    generate_image(data,image_path)
    plt.show()

if __name__ == "__main__":
     test()






