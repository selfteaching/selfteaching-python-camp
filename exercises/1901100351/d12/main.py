# this is d12 exercise for using wxpy
# date: 2019.10.6
# author by: rtgong

from mymodule import stats_word
import requests
from pyquery import PyQuery
from wxpy import *

bot = Bot()
my_friend = bot.friends().search('慧慧')[0]
my_friend.send('请分享我一篇文章')

@bot.register(my_friend,SHARING)
def get_msg(msg):
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    text = str(dict(stats_word.stats_text_cn(content,10)))
    my_friend.send(text)
        
embed
