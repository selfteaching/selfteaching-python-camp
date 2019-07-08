from wxpy import *
bot = Bot(cache_path= True)

#机器人账号自身
myself =bot.self

my_friend =bot.friends()


@bot.register(my_friend,SHARING)
def get_msg(Message):
    return Message.url


print(get_msg(Message))












