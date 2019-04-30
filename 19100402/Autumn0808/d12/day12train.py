#导入wxpy模块
from wxpy import *

#导入day11中的模块
import requests
from pyquery import PyQuery
from mymodule import stats_word
import getpass

#初始化机器人
bot = Bot()

#找好友
my_friend = bot.friends()

#接收share类信息
@bot.register(my_friend,SHARING)

#提取链接信息，并将词频统计结果返回给好友
def get_msg(msg):
    msg_friend = requests.get(msg.url)
    document = PyQuery(msg_friend.text)
    content = document('#js_content').text()
    reply = stats_word.stats_text(content,100)
    return reply

embed()



