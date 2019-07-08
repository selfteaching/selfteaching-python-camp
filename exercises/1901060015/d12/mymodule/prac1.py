from wxpy import *
import requests
from pyquery import PyQuery
import stats_word

bot = Bot(cache_path= True)

#机器人账号自身
myself =bot.self

my_friend =bot.friends()
msg = bot.messages

@bot.register(my_friend,SHARING)
def get_msgurl(msg):
    return Message.url

print(msg)






    
    















