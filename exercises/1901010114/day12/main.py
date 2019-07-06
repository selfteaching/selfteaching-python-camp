

import requests
from pyquery import PyQuery
from wxpy import *
# 初始化机器人，扫码登陆
bot=Bot()
#定位好友豆彭

my_friend = bot.friends().search('豆彭')  #定位朋友
#预先注册，利用Bot.register()完成
#Bot.register(chats=None,msg_types=None,except_self=True,run_async=True,enable=True)
@ot.register(chats='豆彭', msg_types=SHARING)
def auto_reply(msg):
    import requests
   
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    
    msg1 = a(content,100)
    return msg1
embed()