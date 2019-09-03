import json
import stats_word
import jieba
import requests
from pyquery import PyQuery
from wxpy import *
bot = Bot()
my_friend = bot.friends().search('****')[0]
@bot.register(my_friend, SHARING)
def wxpy_stats_word(Message):
        message_url = Message.url
        response = requests.get(message_url)
        document = PyQuery(response.text) 
        content = document('#js_content').text()
        contents = [str(stats_word.stats_text_cn(content,100))]
        my_friend.send(contents)

embed()