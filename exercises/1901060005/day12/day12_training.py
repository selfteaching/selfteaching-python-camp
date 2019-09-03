# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()
my_friend = bot.friends()
# 发送文本给好友
#my_friend.send('Hello WeChat!')

from pyquery import PyQuery
import yagmail
import getpass
import requests
from mymodule import d11_stats_word as sw
@bot.register(my_friend,SHARING) #接受share类信息
def reply_my_friend(msg):
    response = requests.get(msg.url)   
    document = PyQuery(response.text)    
    content = document('#js_content').text()
    #URL信息提取
    reply = sw.stats_text(content,100)
    return reply
    print(reply)
embed() #保持监听状态