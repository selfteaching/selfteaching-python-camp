from mymodule import stats_word
from pyquery import PyQuery
from wxpy import *
import json
import requests

bot = Bot()
#find friend
my_friend = bot.friends()
print(my_friend)

#send text to friend
#my_friend.send("跟我说几句话，随便打几个字")


# auto reply my_friend message (优先匹配后注册的函数!)
# @bot.register(my_friend)
# def auto_reply_my_friend(msg):
#     return 'received:{}({})'.format(msg.text, msg.type)



#monitor and auto_reply all_firend message
@bot.register()
def print_others(msg):
    print(msg) 
    msg.reply(msg)

@bot.register(my_friend,SHARING) #接收sharing信息
def auto_reply(msg):
    sharing_text = requests.get(msg.url) 
    document = PyQuery(sharing_text.text)
    content = document('#js_content').text()
    reply1 = stats_word.stats_text(content,10)
    print(reply1)
    return reply1
embed()
    