from wxpy import *
bot = Bot(cache_path= True)

#机器人账号自身
myself =bot.self

my_friend =bot.friends().search('龙')[0]


@bot.register()
def print_friend_msg(mgs):
    print(mgs)






