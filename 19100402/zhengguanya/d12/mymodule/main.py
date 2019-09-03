#!/usr/bin/python3

import stats_word
import requests
import logging
logging.captureWarnings(True)
from pyquery import PyQuery
from wxpy import *
bot = Bot()
myself = bot.self
my_friend = bot.friends()  
@bot.register(my_friend,SHARING)    
def reply_my_friend(msg):    
    r = requests.get(msg.url)   
    document = PyQuery(r.text)  
    content = document('#js_content').text()
    stats = stats_word.stats_text_cn(content)
    return stats
embed()





