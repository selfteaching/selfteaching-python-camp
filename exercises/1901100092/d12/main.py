from mymodule import stats_word
from pyquery import PyQuery
import requests
import getpass
from wxpy import *

bot = Bot(cache_path = True)
friend = bot.friends()
@bot.register(friend,SHARING)
def load_file(msg):
    response = requests.get(url = msg.url)

    document = PyQuery(response.text)
    content = document('#js_content').text()
    i = str(stats_word.stats_text_cn(content))
    msg.reply(i)
embed()