

from stats_word import stats_text_cn
import requests
from pyquery import PyQuery
# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()
my_friend = bot.friends()
@bot.register(chats=my_friend,msg_types=SHARING,except_self=True,run_async=True,enabled=True)


def reply_msg(msg):
    response = requests.get(msg.url) 
    document = PyQuery(response.text) 
    content = document('#js_content').text()
    result = stats_text_cn(content,20)
    result1 = str(result)
    return result1

embed()