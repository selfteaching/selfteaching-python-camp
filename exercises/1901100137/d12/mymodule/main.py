import stats_word
import yagmail
import requests
import pyquery
import getpass


import pyquery
from pyquery import PyQuery
import wxpy
from wxpy import *
bot = Bot()
my_friend = bot.friends()
@bot.register(my_friend,SHARING)
def reply_message(msg):
    resp= requests.get('msg.url')
    document = PyQuery(resp.text) 
    content = document('#js_content').text()

    result=stats_word.stats_text_cn(content,100)
    result1=str(result)
    return result1
embed()
