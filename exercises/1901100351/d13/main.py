
# this is d13 exercise for using wxpy
# date: 2019.10.19
# author by: rtgong

from os import path

import logging
import requests
import pyquery
import logging
import matplotlib.pyplot as plt
import numpy as np
from mymodule import stats_word
from wxpy import *


cwd = path.abspath(path.dirname(__file__))  # 获取当前工作目录
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文字体



logging.basicConfig(format='file:%(filename)s|line:%(lineno)s|message:%(message)s',level=logging.DEBUG)

def get_article(url):
    r = requests.get(url)
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()

def generate_image(data,image_path):
    labels = [v[0] for v in data]
    widths = [v[1] for v in data]
    ypos = range(len(data))
    fig, ax = plt.subplots()
    ax.barh(ypos,widths)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_ylabels('关键字')
    ax.set_xlabel('词频')
    ax.set_title('The top 10 words in the article')
    fig.savefig(image_path, bbox_inches = 'tight')

def main():
    bot = Bot()
    friends = bot.friends()
    
    @bot.register(friends,SHARING)

    def handler(msg):
        try:
            logging.info('sharing url = %s', msg.url)
            article = get_article(msg.url)
            result = stats_word.stats_text_cn(article,10)
            image_path = path.jion(cwd, 'stats.png')
            generate_image(result, image_path)
            msg.reply_image(image_path)

        except Exception as e:
            logging.exception(e)
    embed

def test():
    article = get_article('https://mp.weixin.qq.com/s/plmuGoc4b2rMN17MSoWgiA')
    result = stats_word.stats_text_cn(article,10)
    image_path = path.jion(cwd, 'stats.png')
    generate_image(result, image_path)

if __name__=="__main__":
    test()
