from wxpy import *
import requests
import itchat
from pyquery import PyQuery 
from mymodule import stats_text
from mymodule import plot_wordsfreq
import matplotlib.pyplot as plt
import numpy as np
# 初始化机器人，扫码登陆

bot = Bot(cache_path=True)

@bot.register()
def print_message(msg):
    if msg.type == 'Sharing': #sharing 分享的公众号文章
        response=requests.get(msg.url)
#         document = PyQuery(response.text)
#         content_input = document('#js_content').text()
#         result_str = stats_text(content_input,10)
        
#         msg.reply('bar1.png') # 自动回复返回的参数
        file=plot_wordsfreq(response,10)
        msg.reply_image(file)# 回复 my_friend 发送的消息
#         msg.send_image('bar1.png')
       
        
 
