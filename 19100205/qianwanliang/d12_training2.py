from wxpy import *
from pyquery import PyQuery
import requests
import mymodule.stats_word
bot = Bot()
my_friend = bot.friends().search('阳')[0]
my_friend.send('hi')

@bot.register('阳')
def get_msg (msg) :
    if msg.type == 'Sharing' :
        response = requests.get(msg.url)
        document = PyQuery(response.text) 
        content = document('#js_content').text()
        result = mymodule.stats_word.stats_text_cn(content, 10)
        convert_result_to_str = ''.join(str(i) for i in result)
        my_friend.send(convert_result_to_str)
    else :
        pass
embed()