
from collections import Counter
import re
import jieba
import json
from wxpy import *
import requests
import itchat
from pyquery import PyQuery 
from mymodule import stats_text
from mymodule import plot_wordsfreq
import matplotlib.pyplot as plt
import numpy as np


bot = Bot(cache_path=True)

@bot.register()
def print_message(msg):
    if msg.type == 'Sharing': #sharing 分享的公众号文章
        response=requests.get(msg.url)
        file=plot_wordsfreq(response,10)
        msg.reply_image(file)# 回复 my_friend 发送的消息

       