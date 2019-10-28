from mymodule import stats_word
import  yagmail
import  requests
import pyquery
import getpass
from os import path
from wxpy import *
from pyquery import PyQuery
import numpy as np      #导入科学计算模块
import matplotlib.pyplot as plt     #导入绘图API
import logging
cwd = path.abspath(path.dirname(__file__))
plt.rcParams['font.sans-serif'] = 'simHei'
def get_article(url):
    r = requests.get(url)   #获取链接
    document = PyQuery(r.text)
    return document('#js_content').text()


# 生成图片
def generate_image(data, image_path):
    plt.rcParams['font.sans-serif'] =["KaiTi"]# 中文乱码的处理
    plt.rcParams['axes.unicode_minus'] = False
    labels = [v[0] for v in data]   
    widths = [v[1] for v in data]
    ypos = range(len(data))  # 获取y轴有多少元素，就生成多少行
    fig, ax = plt.subplots()  # 初始化一个图标
    ax.barh(ypos, widths)  # ax就是生成的坐标系
    ax.set_yticks(ypos)
    ax.set_yticklabels(labels)#设置 y 轴的标签名称
    ax.invert_yaxis() # 反转 y 轴
    ax.set_xlabel('词频')
    ax.set_title('词频统计')
    fig.savefig(image_path, bbox_inches='tight')
    plt.show() #显示此图表
def main():
    bot = Bot()
    friends = bot.friends()

    @bot.register(friends,SHARING)

    def handler(msg):
        try:
            article = get_article(msg.url)
            result = stats_word.stats_text_cn(article,100)
            logging.info('sharing url = %s',msg.url)
            msg.replay(str(result))
        except Exception as e:
            logging.exception(e)
    embed()

def test():
    article = get_article('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    result = stats_word.stats_text_cn(article,20)
    image_path = path.join(cwd,'stats.png')
    generate_image(result,image_path)
if __name__ == "__main__":
    
    test() 


