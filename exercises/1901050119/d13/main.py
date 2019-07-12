import requests
from pyquery import PyQuery
from wxpy import *
from mymodule import stats_word
import matplotlib.pyplot as plt
import numpy as np
from os import path

#获取当前工作目录
cwd = path.abspath(path.dirname(__file__))

#设置中文字体
plt.rcParams['font.sans-serif'] = 'SimHei'

#提取微信公众号文章正文
def get_text(url):   
    response = requests.get(url)
    document = PyQuery(response.text)
    return document('#js_content').text()

#生成图片
def generate_image(data, image_path):
    
    labels = [v[0] for v in data]
    widths = [v[1] for v in data]
    ypos = range(len(data))
    fig, ax = plt.subplots()
    ax.barh(ypos, widths)
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels)
    #ax.invert_yaxis()
    ax.set_ylabel('关键字')
    ax.set_xlabel('词频')
    ax.set_title('词频统计')
    fig.savefig(image_path, bbox_inches = 'tight')


def main():
    bot = Bot()
    friends = bot.friends().search('Galaxy', sex = FEMALE, city = "西安")
    
    @bot.register(friends, SHARING)
    def handler(msg):
        content = get_text(msg.url)
        result = stats_word.stats_text_cn(content, 20)
        image_path = path.join(cwd, 'stats.png')
        generate_image(result, image_path)
        msg.reply_image(image_path)  
    embed()


def test():
    content = get_text('https://mp.weixin.qq.com/s/6uoWKag3TYLdJABtQOIIxg')
    result = stats_word.stats_text_cn(content, 20)
    image_path = path.join(cwd, 'stats.png')
    generate_image(result, image_path)

if __name__ == "__main__":
    main()
    #test()
