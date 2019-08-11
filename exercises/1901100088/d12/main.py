from mymodule import stats_word
import os
import requests
from pyquery import PyQuery
import getpass
import yagmail
from wxpy import *


bot = Bot()
my_friend = bot.friends()

@bot.register(chats=my_friend, msg_types=SHARING, except_self=False)
def get_data(mes):

    response = requests.get(mes.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    outcome = str(stats_word.stats_text_cn(content,100))
    print(outcome)
embed()


