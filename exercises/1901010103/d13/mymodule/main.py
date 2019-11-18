# coding=utf8
#!/usr/bin/python
from wxpy import *
import sys
import matplotlib.pyplot as plt
import numpy as np
from pyquery import PyQuery
sys.path.append('/Users/Yang/GitHub:PJ1/selfteaching-python-camp/exercises/1901010120/d13/mymodule/')
import requests
from stats_word import stats_text
from os import path

#注册机器人
wechat_bot = Bot()
#注册内容是分享就抽取
@wechat_bot.register(chats=User, msg_types=SHARING)
def process_url(msg):
    content_url = msg.url
    html_code = requests.get(content_url).text
    document = PyQuery(html_code)
    content = document("#js_content").text().replace("\n", "")

    try:
        en_result, cn_result = stats_text("", content)
        # print(cn_result)
        msg.reply(cn_result)

        np.random.seed(20190828)
        plt.rcdefaults()
        fig, ax = plt.subplots()

        words = tuple([word for word, count in cn_result])
        y_pos = np.arange(len(words))
        performance = np.array([count for word, count in cn_result])
        error = np.random.rand(len(words))

        ax.barh(y_pos, performance, xerr=error, align="center")
        ax.set_yticks(y_pos)
        ax.set_yticklabels(words, fontproperties='SimHei')
        ax.invert_yaxis()
        ax.set_xlabel("Frequency")
        ax.set_title("Top 20 Chinese words in an article")

        plt.show()

    except ValueError as e:
        print("Exception catched.")
        print(e)

embed()
