from mymodule import stats_word
from pyquery import PyQuery
from wxpy import *
import requests
import matplotlib.pyplot as plt
import numpy as np

bot = Bot()
my_friend = bot.friend().search('夏聪聪',sex=MALE,city='')[0]
my_friend.send('这是一个程序测试，请给我发一篇公众号文章。')

@bot.register(my_friend)
def print_others(msg):
    if msg.type == 'sharing':
        r = requests.get(msg.url)
        document = PyQuery(r.text)
        text = document('#js_content').text()
        content_list = stats_word.stats_text_cn(text,10)
        content_dict = dict(content_list)
        keys,values = zip(*content_dict.items())

        plt.rcdefaults()
        fig, ax = plt.subplots()

        people = content_list
        y_pos = np.arange(len(people))
        error = np.random.rand(len(people))
        word_frequency = values

        plt.rcParams["font.sans_self"] = ["SimHei"]
        ax.barh(y_pos, word_frequency,xerr=error,align="center",color="green",ecolor="black")
        ax.set_yticks(y_pos)
        ax.set_yticklabels(keys)
        ax.invert_yaxis()
        ax.set_xlabel("次数")
        ax.sex_title("文章词频统计如下")

        plt.savefig("d13.png")
        msg.reply_image("d13.png")
embed()