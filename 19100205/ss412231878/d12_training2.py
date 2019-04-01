from wxpy import *
from pyquery import PyQuery
import requests
from mymodule import stats_word

def main():
    bot = Bot()
    my_friend = bot.friends()

    @bot.register(msg_types=SHARING)
    def reply_my_friend(msg):
        wechat = requests.get(msg.url)
        document = PyQuery(wechat.text)
        content = document('#js_content').text()
        wx = stats_word.stats_text(content)
        wechat_word = ''.join(str(i) for i in wx)
               
        return wechat_word

    embed()

if __name__=='__main__':
    main()