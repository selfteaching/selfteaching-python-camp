#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery
from wxpy import *

import stats_word

bot = Bot()
friend_name = input('请输入好友的备注名:')
my_friend =bot.friends().search(friend_name)[0]

@bot.register(my_friend, msg_types='Sharing')
def print_messages(msg): 
    #提取Sharing类型文章的正文
    r = requests.get(msg.url)
    document = PyQuery(r.text)
    content = document('#js_content').text()
    #统计词频
    result = stats_word.stats_text_cn(content,100,len_size = 2)
    result_str = ""
    for i in result:
        result_str += str(i)
    print("统计结果为：", result_str)
    #回复统计结果
    msg.reply(result_str) #也可以写成： return result_str

embed()
