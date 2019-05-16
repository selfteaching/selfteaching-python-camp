from pyquery import PyQuery as pq
import requests
from mymodule import stats_word
from wxpy import *

bot = Bot(console_qr=True)

my_friend = bot.friends().search('QQ')[0]
my_friend.send('你好！')

@bot.register(my_friend)
def step1(msg):
        print(msg.url)
        if msg.type == 'Sharing':
                response = requests.get(msg.url)
                document = pq(response.text)
                content = document('#js_content').text()
                result = stats_word.stats_text_cn(content,100)
                return result
embed()

