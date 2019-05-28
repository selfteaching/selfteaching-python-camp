from pyquery import PyQuery
import requests
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)

@bot.register(Friend,SHARING)
def reply(msg):
    print(msg)
    response= requests.get(msg.url)
    document = PyQuery(response.text) 
    content = document('#js_content').text()
    from stats_word_d12 import stats_text_cn
    result=str(stats_text_cn(content))
    return result
embed()





