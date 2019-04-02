from mymodule import stats_word as sw
import requests
from pyquery import PyQuery
from wxpy import *

bot = Bot() #扫码登录微信

my_friend = bot.friends() #定义好友变量

@bot.register(my_friend,SHARING) #接收share类信息
def auto_reply(msg):
    msg_from_friend = requests.get(msg.url) 
    document = PyQuery(msg_from_friend.text)
    content = document('#js_content').text()
    #URL信息提取
    reply = sw.stats_text(content,count=100)
    return reply #将词频自动发给好友

embed() #保持监听状态