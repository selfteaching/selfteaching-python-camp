import requests
from pyquery import PyQuery
from mymodule import stats_word
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from pylab import mpl
myfont = matplotlib.font_manager.FontProperties(fname="Light.ttc")
mpl.rcParams['font.sans-serif'] = ['Fangsong']
mpl.rcParams['axes.unicode_minus'] = False
from wxpy import *
bot = Bot()

@bot.register(msg_types = SHARING)

def auto_reply(msg):
    r = requests.get(msg.url)
    document = PyQuery(r.text)
    content = document('#js_content').text()
    result = stats_word.stats_text_cn(content)
    file = eval(result)
    words = []
    counts = []
    for item in file:
        words.append(item[0])
        counts.append(item[1])
    words = tuple(words)
    fig, ax = plt.subplots(figsize=(20,60))
    y_pos = np.arange(len(words))
    counts = np.array(counts)
    error = np.random.rand(len(words))

    ax.barh(y_pos, counts, xerr=error, align='center', color='green', ecolor='black')

    ax.set_yticks(y_pos)

    ax.set_yticklabels(words)

    ax.invert_yaxis()
    ax.set_xlabel('counts')
    ax.set_title('Analysis of Chinese word frequency')

    plt.savefig("word_frequency_chart.jpg")
    msg.reply_image("word_frequency_chart.jpg")


embed()