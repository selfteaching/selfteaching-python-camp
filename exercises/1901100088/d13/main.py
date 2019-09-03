from mymodule import stats_word
import os
import requests
from pyquery import PyQuery
import getpass
import yagmail
from wxpy import *
import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()

def main():

    bot = Bot()
    my_friend = bot.friends()

    @bot.register(chats=my_friend, msg_types=SHARING, except_self=False)
    def send_fig(mes):

        response = requests.get(mes.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        outcome = stats_word.stats_text_cn(content,20)
        
        word = [l[0]for l in outcome]
        nub = [l[1]for l in outcome]
        y_pos = np.arange(len(word))

        plt.rcParams['font.sans-serif'] = 'SimHei'
        fig, ax = plt.subplots()
        
        ax.barh(y_pos, nub, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(word)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Number')#x轴标签
        ax.set_title('The most frequent word')#标题设定
        plt.savefig("fig.png")

        mes.reply_image("fig.png") 
    embed()

if __name__ == "__main__":
    main()