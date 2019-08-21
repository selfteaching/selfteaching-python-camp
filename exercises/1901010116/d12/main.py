from mymodule import stats_word
from pyquery import PyQuery
from wxpy import *
import requests


#提取微信公众号文章
def get_article(url):
    r = requests.get(url)
    document = PyQuery(r.text)
    return document('#js_content').text()

def main():
    #初始化机器人，扫码登陆
    bot = Bot()
    friends = bot.friends()
    @bot.register(friends,SHARING)
    def handler(msg):
        article = get_article(msg.url)
        result = stats_word.stats_text_cn(article,100)
        msg.reply(str(result))
    embed()

if __name__ == '__main__':
    main()