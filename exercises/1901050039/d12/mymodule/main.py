from wxpy import *
import requests
from pyquery import PyQuery
import stats_word
bot = Bot()

@bot.register()   #回复信息
def auto_reply(msg): 
    if msg.type == 'Sharing':    #设条件，是微信公号文章的就进行词频分析
        r = requests.get(msg.url)
        document = PyQuery(r.text)
        content = document('#js_content').text()
        result = str(stats_word.stats_text_cn(content))
    return result

embed()