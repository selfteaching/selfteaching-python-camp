import requests
from pyquery import PyQuery
from wxpy import *
from mymodule import stats_word

# 初始化机器人，扫码登陆
bot = Bot()

@bot.register()
def word_count(msg):
    if msg.type == 'Sharing':
        r = requests.get(msg.url)
        document = PyQuery(r.text)
        content = document('#js_content').text()
        word_list = stats_word.stats_text_cn(content, 20)
        content = document('#js_content').text()
        msg.sender(str(word_list))
    elif msg.type == 'Text':
        msg.sender("还给你: " + msg.text)
    else:
        msg.sender("不理你")

embed()