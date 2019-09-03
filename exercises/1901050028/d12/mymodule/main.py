import stats_word
import json
import requests
from pyquery import PyQuery
from wxpy import Bot,Message,embed,SHARING

bot = Bot() #扫码登录微信
my_friend = bot.friends() #定义好友变量

@bot.register() #接收share类信息
def auto_reply(msg):
        if Message.type== 'sharing':
                r = requests.get(msg.url) 
                document = PyQuery(r.text)
                content = document('#js_content').text()
                reply = stats_word.stats_text(content,count=100)
                return reply #将词频自动发给好友

embed() #保持监听状态