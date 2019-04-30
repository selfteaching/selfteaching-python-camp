'''这是一个利用wxpy功能自动完成微信登录和获取好友转发的网址信息，
将信息中的主要内容提取及获取词频反馈，并把结果发给好友的程序'''

import training1
from wxpy import *

'''登录微信'''
bot = Bot()

'''选取特定的对象小明'''
object1 = bot.friends().search('小明')[0]
'''接受好友发来的类型为分享的信息后，将分享网址中内容的词频统计前100个发给对方'''
if object1.Message.type == 'Sharing':
    url = Message.url
    object1.sent(training1.stats_meg(url))
else:
    print("您的好友还没发给您关于分享类型的信息")