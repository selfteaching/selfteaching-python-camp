from wxpy import *
bot = Bot(cache_path= True)

#机器人账号自身
myself =bot.self

@bot.register()
def print_group_msg(mgs):
    print(mgs)



