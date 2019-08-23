import sys
import os
import jieba
import wxpy
from wxpy import *
import requests 
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot,savefig
plt.rcParams['font.sans-serif']=['SimHei']
from pyquery  import PyQuery
from collections import Counter
sys.path.append('E:\self-teaching\selfteaching-python-camp\exercises\1901100167\d12\mymodule')
from mymodule import stats_word
bot=Bot()
myself=bot.self
bot.file_helper.send('Hello from wxpy!')
friends=bot.friends()
@bot.register(friends,SHARING)
def url(msg):
    r=requests.get(msg.url)
    document=PyQuery(r.text)
    content=document('#js_content').text()
    a=stats_word.stats_text_cn(content)
    b=Counter(dict(a))
    k=list(b)
    v=list(b.values())
    plt.bar(k,v)
    plt.xlabel('词语')
    plt.ylabel('次数')
    plt.title('高频词统计')
    plt.show()
    plt.savefig('C:\\Users\\Administrator\\Desktop\\a.jpg',bbox_inchs = 'tight')
    msg.reply_image('C:\\Users\\Administrator\\Desktop\\a.jpg')
embed()




