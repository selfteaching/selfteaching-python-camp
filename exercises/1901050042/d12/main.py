import stats_word
import requests
from pyquery import PyQuery
from wxpy import *

bot = Bot()

my_friend = bot.friends().search('Daybreak', sex=MALE, city="北京")[0]
my_friend.send("你好！")

@bot.register(my_friend)
def step1 (msg):
    if msg.type == 'Sharing':
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('#js_content').text()
        result = stats_word.stats_text_cn(content,100)
        return result

embed()