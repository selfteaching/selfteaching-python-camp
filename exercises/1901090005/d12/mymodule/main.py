
import stats_word
import requests
import pyquery
import wxpy
count = 100
from wxpy import *
bot = Bot()
my_friend = bot.friends().search('煜鹏')[0]

my_friend.send("this is a test")

@bot.register(my_friend,SHARING)
def auto_reply(msg):
    print(msg.url)
    reponse = requests.get(msg.url)
    from pyquery import PyQuery
    document = PyQuery(reponse.text)
    content = document('#js_content').text()
    string = str(stats_word.stats_text_cn(content,count))
    return string
    #my_friend.send(string)
embed()




