


from mymodule.stats_word import stats_text_cn
from mymodule.utils import request, send_email
import json
from wxpy import *
import matplotlib.pyplot as plt
import numpy as np
# 1. 登录微信,监听好友信息,获取好友的发的链接
# 2. 使用词频统计函数
# 3. 将结果发给发链接的好友
bot = Bot()

# 打印来自其他好友、群聊和公众号的消息

@bot.register()
def print_others(msg):
    # print(msg.type, msg.text)
    if msg.type == 'Sharing':
        print('chat',msg.chat)
        print('sender',msg.sender)
        print(msg.text, msg.url)
        # 处理并返回
        text = request(msg.url)
        res = stats_text_cn(text,100)
        res =json.dumps(res,ensure_ascii=False)
        msg.reply(res)
    print(msg)

@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')
embed()
