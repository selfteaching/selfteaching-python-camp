import sys
import os
import jieba
import wxpy
from wxpy import *
import requests 
from pyquery  import PyQuery
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
    msg.reply(a)
    return a
embed()


