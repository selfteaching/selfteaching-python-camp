
from collections import Counter
import re
import jieba
import json
from wxpy import *
import requests
import itchat
from pyquery import PyQuery 
import matplotlib.pyplot as plt
import numpy as np
import stats_word

bot = Bot(cache_path=True)


@bot.register()
def print_message(msg):
    if msg.type == 'Sharing': #sharing 分享的公众号文章
        r = requests.get(msg.url) #解析获取公众号文章的url
        document = PyQuery(r.text)
        content = document('#js_content').text()
        r_list = stats_word.stats_text(content,100)
        r_str = str(r_list)
        msg.reply(r_str) # 自动回复返回的参数

