# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 16:48:52 2019

@author: PetalSaya
"""
import stats_word
import requests
from pyquery import PyQuery
from wxpy import *

bot = Bot()

my_friend = bot.friends().search('Daybreak', sex=MALE, city="成都")[0]
my_friend.send("随便转发一篇文章给我行不？")

@bot.register(my_friend)
def step1 (msg):
    if msg.type == 'Sharing':
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        result = stats_word.stats_text_cn(content,100)
        return result

embed()