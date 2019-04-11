from mymodule import stats_word
import requests
from pyquery import PyQuery
from wxpy import * 
bot = Bot()
@bot.register()
def new_message(msg):
    if msg.type=='Sharing':
        response=requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        freq=stats_word.stats_txt(content,10)
        freq=str(freq)
        msg.reply('此文章十大高频用词')
        msg.reply(freq)
    
embed()

