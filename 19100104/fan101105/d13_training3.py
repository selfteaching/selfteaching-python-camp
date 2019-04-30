from mymodule import stats_word
import requests
from pyquery import PyQuery
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np 

bot = Bot()
myfriend1 = bot.friends().search('alan')[0]
if myfriend1.Message.type == 'Sharing':
    url = Message.url
    response = requests.get(url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    top100=str((stats_word.stats_txt_cn(content)))
    
    np.random.seed(19680801)
    plt.rcdefaults()
    fig, ax = plt.subplots()

    # 对数据进行处理
    cipin=(top100[0])
    y_pos = np.arange(len(cipin))
    performance = 3 + 10 * np.random.rand(len(cipin))
    error = np.random.rand(len(cipin))
    #图表设置内容
    ax.barh(y_pos, performance, xerr=error, align='center',
            color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(cipin)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('TOP100词频统计结果')
    ax.set_title('你分享的文章热词统计')

    plt.savefig('cipin.png')
    msg.reply_image('cipin.png')