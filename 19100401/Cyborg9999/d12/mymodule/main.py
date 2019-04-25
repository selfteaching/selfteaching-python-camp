from wxpy import *
import main2

bot = Bot()


my_friend = bot.friends().search('程跃Pro')



@bot.register(my_friend,SHARING)
def auto_reply(msg):
        url = msg.url
        stats_msg = main2.stats(url)
        msg.reply(stats_msg)
    
embed()