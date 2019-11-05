# 从mymodule文件夹中调用stats_word.py
from mymodule import stats_word
from pyquery import PyQuery
from wxpy import *
import requests

if __name__ == "__main__":
    try:
        bot = Bot()
        my_friend = bot.friend().search('夏聪聪',sex=MALE,city='')[0]
        my_friend.send('这是一个程序测试，请给我发一篇公众号文章。')

        @bot.register()
        def print_other(msg):
            if msg.type == 'sharing':
                r = requests.get(msg.url)
                document = PyQuery(r.text)
                text = document('#js_content').text()
                content = stats_word.stats_text_cn(text,100)
                msg.reply(content)
    except ValueError:
        print('The input is a non-string, please enter a string.')