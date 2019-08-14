from mymodule import stats_word
import requests
from pyquery import PyQuery
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np
import os

def getarticle(url):
    r = requests.get(url)
    document = PyQuery(r.text)
    return document('#js_content').text()

def main():
    bot = Bot()
    my_frinds = bot.friends().search('brian')[0]
    @bot.register(my_frinds)
    def reply_statistic(msg):
        if  msg.type == 'Sharing':
           texturl = msg.url          # 获取分享内容的链接
           text = getarticle(texturl) 
           replay_content = stats_word.stats_text_cn(text, 100)

           text_y = tuple([row[0] for row in replay_content])
           text_x = tuple([row[1] for row in replay_content])

           plt.rcdefaults()
           plt.rcParams['font.sans-serif'] = ['STFangsong']
           plt.rcParams['axes.unicode_minus'] = False
           fig, ax = plt.subplots()
           fig = plt.figure(figsize=(5,20))
           y_pos = np.arange(len(text_y))
           ax = fig.add_subplot(111)
           ax.barh(y_pos, text_x, align='center')
           ax.set_yticks(y_pos)
           ax.set_yticklabels(text_y)
           ax.invert_yaxis()  # labels read top-to-bottom
           ax.set_xlabel('出现次数')
           ax.set_title('出现频率最高的前100个词')
           plt.savefig('words_frequency.png')
           msg.reply_image('words_frequency.png')
           # os.remove('words_frequency.png')
    embed()

if __name__ == '__main__':
    main()
