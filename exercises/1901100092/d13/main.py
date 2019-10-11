from mymodule import stats_word
from pyquery import PyQuery
import requests
import getpass
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np

bot = Bot(cache_path = True)
friend = bot.friends()
@bot.register(friend,SHARING)
def load_file(msg):
    response = requests.get(url = msg.url)

    document = PyQuery(response.text)
    content = document('#js_content').text()
    i = str(stats_word.stats_text_cn(content))
    
    plt.rcdefaults()
    figure, ax = plt.subplots()

    plt.rcParams['font.sans-serif'] = ['SimHei']

    dict_i = dict(i)
    x_values = []
    y_values = []
    for k,v in dict_i.items():
        x_values.append(k)
        y_values.append(v)
    y_pos = np.arange(len(x_values))
    error = np.random.rand(len(x_values))

    ax.barh(y_pos, y_values, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(x_values)
    ax.invert_yaxis() 
    ax.set_xlabel("汉字")
    ax.set_ylabel("出现次数")
    ax.set_title("词频统计图")
    plt.savefig("词频统计图.png")    

    msg.reply_image("词频统计图.png")

embed()



