import requests
from pyquery import PyQuery
from mymodule import stats_word
from wxpy import *
bot = Bot()

@bot.register(msg_types = SHARING)

def auto_reply(msg):
    r = requests.get(msg.url)
    document = PyQuery(r.text)
    content = document('#js_content').text()
    result = stats_word.stats_text_cn(content)
    msg.reply(result)

embed()