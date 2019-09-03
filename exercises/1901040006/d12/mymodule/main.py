import stats_word
import requests
from pyquery import PyQuery as pq
from wxpy import *

bot = Bot()

@bot.register(Friend, SHARING)
def auto_reply(msg):
    r = requests.get(msg.url)
    document = pq(r.text)
    content = document('#js_content').text()
    #统计词频
    result = stats_word.stats_text(content,0,100)
    return result
embed()







