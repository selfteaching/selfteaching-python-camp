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
        freq=stats_word.stats_txt(content,100)
        freq=str(freq)
        msg.reply(freq)
    
embed()

