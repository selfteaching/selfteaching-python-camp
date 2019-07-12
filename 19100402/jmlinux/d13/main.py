from mymodule import stats_word
from pyquery import PyQuery
from wxpy import *
import getpass
import requests
import matplotlib.pyplot as plt
import numpy as np

bot = Bot()
my_friend = bot.friends()

#my_friend = bot.friends().search("丽丽")[0]
#my_friend.send("请发一篇公众号文章给我，我想给些惊喜你看,返回文章前10个高频词的图表给你")
#print("消息发送成功")

@bot.register(my_friend)
def send_result(msg):
    if msg.type == "Sharing":
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        dict1 = dict(stats_word.stats_text_cn(content,10))
        np.random.seed(19680801)
        plt.rcdefaults()
        fig, ax = plt.subplots()
        words,nums = zip(*dict1.items())
        y_pos = np.arange(len(words))
        performance = nums
        error = np.random.rand(len(words))
        plt.rcParams['font.sans-serif']=['SimHei'] 
        ax.barh(y_pos, performance, xerr=error, align='center',
        color='red', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(words)
        ax.invert_yaxis()  
        ax.set_xlabel('word frequency')
        ax.set_title('The first ten words of the article')
        #plt.show()
        plt.savefig("result.jpg")
        msg.reply_image('result.jpg')

embed()