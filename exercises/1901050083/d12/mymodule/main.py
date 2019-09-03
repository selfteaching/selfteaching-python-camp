import stats_word
import re
import json
from os import path
import requests
from pyquery import PyQuery
import yagmail
from wxpy import *

bot = Bot(cache_path = True)
my_friend = bot.friends().search('那个谁')[0]
tuling = Tuling(api_key='XXXXXXXXXXXXXXXXXXXXXXX')
@bot.register(my_friend, except_self = True)


def auto_reply(msg):
    print (msg.sender.name,':',msg.text,'Msg Type:',msg.type, msg.url)
    msg.sender.mark_as_read()
    if msg.type == SHARING:
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        count=20
        most_20=stats_word.stats_text_cn(content, count)
        aaaaa=str(most_20)
        print (aaaaa)
        return "刚才那篇文站出现次数最多的前20个词是" + aaaaa

    else:
        tuling.do_reply(msg)

embed()

 

