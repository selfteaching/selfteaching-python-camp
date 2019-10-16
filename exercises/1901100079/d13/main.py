from mymodule import stats_word
import logging
import pyquery
import requests
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np
from os import path

cwd=path.abspath(path.dirname(__file__))
plt.rcParams['font.sans-serif']='SimHei' # 中文字体

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG) 
# %(filename)s: 打印当前执行程序名；%(lineno)d: 打印日志的当前行号；%(message)s: 打印日志信息；level: 设置日志级别，debug是打印全部的日志,详细的信息,通常只出现在诊断问题上。

def get_artical(url):
    art=requests.get(url) 
    doc=pyquery.PyQuery(art.text)
    return doc('#js_content').text()

def figure(d,image_path):
    fig, ax = plt.subplots()
    y=[r[0] for r in d]
    x=[r[1] for r in d]
    y_pos = np.arange(len(d))
    ax.barh(y_pos, x, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(y)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('词频')
    ax.set_ylabel('统计词')
    ax.set_title('文章词频统计图')
    fig.savefig(image_path,bbox_inches='tight')


def main():
    bot=Bot()
    my_friend=bot.friends()
    @bot.register(my_friend,SHARING)
    def handler(msg):
        try:
            logging.info('分享的网址是：%s',msg.url)
            a=get_artical(msg.url)
            output=stats_word.stats_text_cn(a,20)
            msg.reply(str(output))
            image_path=path.join(cwd,'word_image.png') 
            figure(output,image_path)
            msg.reply_image(image_path)  
        except Exception as i:
            logging.exception(i)
    embed()

'''def test(): # 测试用
    a=get_artical('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    output=stats_word.stats_text_cn(a,20)
    image_path=path.join(cwd,'word_image.png') 
    figure(output,image_path)'''

if __name__=='__main__':
    main()         
