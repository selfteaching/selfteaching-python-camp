import requests
from pyquery import PyQuery
import stats_word

from wxpy import *
bot = Bot()
my_friend = bot.friend().search('xx',sex=MALE,city='')[0]
my_friend.send('程序测试，请给我发送一篇文章')


@bot.register()
def print_others(msg):
    if msg.type == 'Sharing':
        r = requests.get(msg.url)
        document = PyQuery(r.text)
        content = document('#js_content').text()
        r_list = stats_word.stats_text(content,100)
        r_str = str(r_list)
        msg.reply(r_str)
embed()