#用来获取微信的分享类消息并返回一个网址给好友

#导入模块
from wxpy import *

#回复消息
def reply_stats():
    bot = Bot()

    @bot.register(msg_types=TEXT)
    def reply_my_friend(msg):
        h = "hello!"
        return h

    embed()
