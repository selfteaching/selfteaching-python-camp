from wxpy import *
import d11_training1
bot = Bot()


my_friend = bot.friends().search('伟仪',sex=FEMALE,city='深圳')[0]
my_friend.send('请小叶子分享文章')


@bot.register(my_friend)
def get_msg(msg):
    if msg.type == 'Sharing':
        target_url = msg.url
        stats_msg = d11_training1.stats(target_url)
        msg.reply(stats_msg)
    else:
        pass
embed()