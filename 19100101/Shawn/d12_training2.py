from wxpy import *
import d12_training1
bot = Bot()

# 找到好友并发消息
my_friend = bot.friends().search('Somebody')[0]
my_friend.send('请给我分享一篇文章')

# 获取分享文章url
@bot.register(my_friend)
def get_msg (msg) :
    if msg.type == 'Sharing' :
        target_url = msg.url
        stats_msg = d12_training1.stats(target_url)
        msg.reply(stats_msg)
    else :
        pass
embed()