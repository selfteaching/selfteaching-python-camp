# Date : 19/03/29

from wxpy import *
import d11_training1
bot = Bot()

# 找到好友并发消息
my_friend = bot.friends().search('三碗饭')[0]
my_friend.send('请给我分享一篇文章')

# 获取分享文章url
@bot.register()
def print_others(msg) :
    if msg.type == 'Sharing' :
        target_url = msg.url
        stats_msg = d11_training1.stats(target_url)
        msg.reaply(stats_msg)
    else :
        pass
embed()