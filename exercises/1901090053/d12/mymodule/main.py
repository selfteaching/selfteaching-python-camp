
import stats_word as sw 
import json
from pyquery import PyQuery
import requests
import yagmail
import getpass
from wxpy import *


bot = Bot(cache_path=True)


my_friend = bot.friends().search('测试员')[0]
my_friend = bot.file_helper
@bot.register(my_friend)
def auto_reply_word_stats(msg):
    r = requests.get(msg.url)
    document = PyQuery(r.text)
    text = document('p').text()
    contents = str(sw.stats_text_cn(text, 100))
    my_friend.send(contents)


bot.join()
bot.logout()
