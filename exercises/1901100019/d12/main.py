from mymodule import stats_word
import requests
from pyquery import PyQuery
from wxpy import *

if __name__ == '__main__':

    bot = Bot(cache_path=True)

    @bot.register()
    def print_messages(msg):
        print(msg)
        if msg.type == 'Sharing':
            r = requests.get(msg.url)
            document = PyQuery(r.text)
            content = document('#js_content').text()
            
            result = stats_word.stats_text_cn(content, 10)
            print(result)
            msg.reply('文章中最常出现的前10个词：' + str(result))

    embed()