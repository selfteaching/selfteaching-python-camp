from wxpy import *
import requests
from pyquery import PyQuery
from chinese import Chinesechar
bot = Bot(console_qr=True,cache_path=True) 
my_friend = bot.friends() 
@bot.register(my_friend,SHARING) 
def auto(msg):
    text = msg.url
    response = requests.get(text) 
    document = PyQuery(response.text)
    content = document('#js_content').text()
    return Chinesechar(content,20) 
embed()
