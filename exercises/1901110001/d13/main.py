from mymodule import stats_word
from pyquery import PyQuery
import yagmail
import getpass
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
from wxpy import *
count = 20
import requests

bot = Bot()

@bot.register(msg_types = SHARING)
def print_group_msg(msg):
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    contents = document('#js_content').text()
    result = str(stats_word.stats_text_cn(contents,20)) 
    fig,ax =plt.subplots()
    file = eval(result)
    print(file)
    words = []
    counts = []
    for item in file:
        words.append(item[0])
        counts.append(item[1])
    words = tuple(words)
    y_pos = np.arange(len(words))
    counts = np.array(counts) 
    error = np.random.rand(len(words))
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False
    ax.barh(y_pos,counts,xerr=error,align='center',color='blue',ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(words)
    ax.invert_yaxis()
    ax.set_xlabel('counts')
    ax.set_title('Analysis of Chinese word frequency')
    plt.savefig('word_frequency_chart.jpg')
    msg.reply_image('word_frequency_chart.jpg') 
embed()
