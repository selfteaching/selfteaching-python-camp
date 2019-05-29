import stats_word
import requests
import pyquery
import wxpy
import matplotlib.pyplot as plt
import numpy as np
count = 10
from wxpy import *
from pylab import mpl
# from matplotlib.font_manager import FontProperties
#plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.rcParams['font.sans-serif'] = 'STFangsong'
mpl.rcParams['axes.unicode_minus'] = False

bot = Bot()
my_friend = bot.friends().search('煜鹏')[0]
my_friend.send("给我发个公众号文章")

@bot.register(my_friend,SHARING)
def auto_reply(msg):
    print(msg.url)
    reponse = requests.get(msg.url)
    from pyquery import PyQuery
    document = PyQuery(reponse.text)
    content = document('#js_content').text()
    string = stats_word.stats_text_cn(content,count)
    tmp = dict(string)
    keys,value = zip(*tmp.items())

    #np.random.seed(19680801)

    #plt.rcdefaults()

    fig, ax = plt.subplots()
    wd = string
    y_pos = np.arange(len(wd))
    error = np.random.rand(len(wd))
    #font = FontProperties(fname='/Library/Fonts/Songti.ttc')
    ax.barh(y_pos, value, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(keys)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('词频数')
    ax.set_title('词频图表')
    plt.savefig("d13.png")
    my_friend.send_image("d13.png")

embed()

   

