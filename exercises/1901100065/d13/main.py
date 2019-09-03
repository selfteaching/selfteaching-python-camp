from mymodule import stats_word
import requests
from pyquery import PyQuery
from wxpy import *
import matplotlib.pyplot as plt
from os import path
from os import remove


# 获取当前工作目录
cwd = path.abspath(path.dirname(__file__))

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['STFangsong']


def getarticle(url):
    r = requests.get(url)
    document = PyQuery(r.text)
    return document('#js_content').text()

def generate_image(data, image_path):
    """
    用于生成词频统计的图片
    """
    text_y = tuple([row[0] for row in data])
    text_x = tuple([row[1] for row in data])
    y_pos = range(len(text_y))
    fig, ax = plt.subplots()
    fig = plt.figure(figsize=(5,20))
    ax = fig.add_subplot(111)
    ax.barh(y_pos, text_x, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(text_y)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('出现次数')
    ax.set_title('出现频率最高的前100个词')
    fig.savefig(image_path, bbox_inches='tight')
   
           

def main():
    bot = Bot()
    my_frinds = bot.friends().search('brian')[0]
    @bot.register(my_frinds)
    def reply_statistic(msg):
        if  msg.type == 'Sharing':
           texturl = msg.url          # 获取分享内容的链接
           text = getarticle(texturl) 
           replay_content = stats_word.stats_text_cn(text, 100)
           image_path = path.join(cwd, 'stats.png')
           generate_image(replay_content, image_path)
           msg.reply_image(image_path)
           remove(image_path)
    embed()

if __name__ == '__main__':
    main()
