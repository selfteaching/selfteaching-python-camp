from mymodule import stats_word
import requests
from pyquery import PyQuery
from wxpy import *

bot=Bot()
my_friend=bot.friends()

@bot.register(my_friend,msg_types=SHARING)

def reply_my_friend(msg):
    response=requests.get(msg.url)
    document=PyQuery(response.text)
    content=document('#js_content').text()
    reply=print(stats_word.stats_text_cn(content,100))
    return reply
       
embed()







    