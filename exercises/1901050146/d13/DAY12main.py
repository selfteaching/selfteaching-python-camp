from mymodule import stats_word
from pyquery import PyQuery
import requests
from wxpy import *
bot = Bot()
my_friend = bot.friends()

@bot.register(my_friend,SHARING)
def reply_my_friend(msg):
    response =requests.get(msg.url)
    document=PyQuery(response.text)
    content=document('#js_content').text()
    a=stats_word.stats_text(content,50)
    return a
embed()