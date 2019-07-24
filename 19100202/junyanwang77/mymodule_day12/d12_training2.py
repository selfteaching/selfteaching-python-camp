from wxpy import *
import d12_training1

bot = Bot()


my_friend = bot.friends().search('金志坚')



@bot.register(my_friend,SHARING)
def auto_reply(msg):
        url = msg.url
        stats_msg = d12_training1.stats(url)
        msg.reply(stats_msg)
    
embed()