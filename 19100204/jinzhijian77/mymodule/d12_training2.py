import d12_training1

from wxpy import *
bot = Bot()
my_friend = ensure_one(bot.friends().search('果果爸爸'))

@bot.register(my_friend,SHARING)
def auto_reply(msg):
        url = msg.url
        stats_msg = d12_training1.stats(url)
        msg.reply(stats_msg)



embed()