import d12_training1

from wxpy import *
bot = Bot()
my_friend = ensure_one(bot.friends().search('果果爸爸'))

@bot.register(my_friend)
def sharing_msg(msg):
    if msg.type == 'sharing':
        url = msg.url
        stats_msg = d12_training1.stats(url)
        
        msg.reply(stats_msg)
    else :
        print("未分享")


embed()