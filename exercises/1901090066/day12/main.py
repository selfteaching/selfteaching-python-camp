from mymodule import state_word
import requests
import yagmail
import getpass
from pyquery import PyQuery
import wxpy
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()
my_friend = bot.friends()
@bot.register(chats=my_friend, msg_types=SHARING, except_self=True, run_async=True, enabled=True)
#注册函数，消息的类型是SHARING类型 
def reply_msg(msg):
       '''定义函数，实现接收微信好友分享的内容，并回复统计的词频。'''
       response = requests.get(msg.url)   #使⽤requests请求信息中的url
       document = PyQuery(response.text)
       content = document('#js_content').text()
       result=state_word.stats_text_cn(content,50)
       result1=str(result)
       return result1
       #在被注册函数中，可以通过直接 return <回复内容> 的方式来回复消息，等同于调用 msg.reply(<回复内容>)
       
embed()
