from wxpy import *
from wxpy.api.messages.message import Message
import d11_training1, d13_training3


# 初始化机器人，扫码登陆
bot = Bot()
# 搜索名称含有 "jack" 的好友
my_friend = bot.friends().search('jack')[0]
# 发送文本给好友
# my_friend.send('在忙什么？')

# 回复消息
# @bot.register(my_friend, SHARING)
# def reply_my_friend(msg):
#     return d11_training1.get_request(msg.url)

# 自动回复消息
@bot.register(my_friend)
def auto_reply(msg):
    if msg.type == "Sharing":
        d13_training3.generate_charts(msg.url)      
        msg.reply_image("./tupian.jpg") 
    else:
        return "稍后电话联系你！"
 
    
embed()


