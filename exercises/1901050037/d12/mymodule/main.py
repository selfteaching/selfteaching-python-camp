from wxpy import *
import requests
import itchat
from pyquery import PyQuery 
from mymodule import stats_text

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)

@bot.register()
def print_message(msg):
    if msg.type == 'Sharing': #sharing 分享的公众号文章
        response=requests.get(msg.url)
        document = PyQuery(response.text)
        content_input = document('#js_content').text()
        result_str = str(stats_text(content_input,100))
        msg.reply(result_str) # 自动回复返回的参数

