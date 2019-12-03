import requests
from pyquery import PyQuery
import stats_word
from wxpy import *
bot = Bot()
my_friend = bot.friends().search("波罗",sex=MALE,city='广州')[0]
my_friend.send('我找到你了')
@bot.register(chats =None,msg_types = 'Sharing',except_self = True)
def auto_reply(msg):
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    list1 = stats_word.stats_text_cn(content,20)
    d1 = dict(list1)
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm
    plt.rcdefaults()
    fig,ax = plt.subplots()
    plt.rcParams['font.sans-serif'] = ['simhei'] 
    people = list(d1.keys())
    y_pos = np.arange(len(people))
    performance = list(d1.values())
    ax.barh(y_pos,performance,xerr=None,align='center',color='green',ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.set_xlabel(performance)
    ax.invert_yaxis()
    ax.set_title('词频排序前20') 
    plt.savefig('day13.png')
    msg.reply_image('day13.png')
    plt.show()
embed()