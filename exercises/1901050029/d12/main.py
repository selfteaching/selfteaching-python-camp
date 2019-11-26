# Filename : main.py
# author by : 张金磊

#import pandas as pd
import yagmail
import requests
import getpass
from mymodule import stats_word
from pyquery import PyQuery as py
from wxpy import *


bot = Bot()
friend_M = bot.friends().search("M.")[0]

@bot.register(friend_M,SHARING)
def auto_get_url(msg):
    response = requests.get(msg.url)
    document = py(response.text) 
    content = document('#js_content').text()
    text_1 = stats_word.stats_text_cn(content,100)
    text_2= str(text_1)
    bot.file_helper.send(text_1)
    return text_2
    
# 堵塞线程，并进入 Python 命令行
embed()




        

 

