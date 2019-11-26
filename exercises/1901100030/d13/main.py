# day13 实战应用
# 2019年7月25日
# 陈浩 学号 1901100030

import logging
import requests
import pyquery
import getpass
from mymodule import stats_word
from os import path
# 导入模块
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np

#获取当前工作目录
cwd = path.abspath(path.dirname(__file__))
# 设置中文字体
plt.rcParams["font.sans-serif"] = "SimHei"

# 初始化logging模块
logging.basicConfig(format="file:%(filename)s|line:%(lineno)d|message:%(message)s",level=logging.DEBUG)

# 获取微信公众号正文
def get_article(url):
    r = requests.get(url)
    document = pyquery.PyQuery(r.text)
    return document("#js_content").text()

# 生成图片
def generate_image(data, image_path):
    labels = [v[0] for v in data]
    width = [v[1] for v in data]
    ypos = range(len(data))
    fig, ax = plt.subplots()
    ax.barh(ypos,width)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel('词频')
    ax.set_ylabel('关键字')
    ax.set_title('词频统计')
    fig.savefig(image_path,bbox_inches="tight")


def main():
    
    # 初始化机器人，扫码登陆
    bot = Bot()
    friends = bot.friends()

    @bot.register(friends, SHARING)
    def handler(msg):
        try:
            article = get_article(msg.url)
            logging.info("sharing url = %s",msg.url)
            data = stats_word.stats_text_cn(article, 10)
            image_path = path.join(cwd, "stats.png")
            generate_image(data,image_path)
            msg.reply_image(image_path)     
        except Exception as e:
            logging.exception(e)
        embed()

def test():
    article = get_article("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
    data = stats_word.stats_text_cn(article, 10)
    image_path = path.join(cwd, "stats.png")
    generate_image(data,image_path)
    plt.show()

if __name__ == "__main__":
    # main()
    test()



