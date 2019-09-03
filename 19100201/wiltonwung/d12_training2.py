import requests
from pyquery import PyQuery
from mymodule import stats_word

from wxpy import *

bot = Bot() 

my_friend = bot.friends()

@bot.register(my_friend)

def SHARING_Msg(msg):
    if msg.type == 'Sharing':
        response = requests.get(msg.url)
        document = PyQuery(response.text) 
        content = document('#js_content').text()  
        c= str(stats_word.stats_text(content, 100))
        msg.reply(c)
    else:
        print('waiting......')

embed()
        