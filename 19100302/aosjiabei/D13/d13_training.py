import requests
from wxpy import *
from pyquery import PyQuery
import matplotlib.pyplot as plt
import numpy as np

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)

@bot.register(Friend,SHARING)#对朋友发的sharing操作
def reply(msg):#注册函数:自动回复
    print(msg)

    #提取sharing正文
    response= requests.get(msg.url)
    document = PyQuery(response.text) 
    content = document('#js_content').text()
    from stats_word_d13 import stats_text_en
    stats_text_en(content)#调用模板,统计
    msg.sender.send_image('result.png') 
embed()





