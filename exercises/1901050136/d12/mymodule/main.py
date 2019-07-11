# this script is to implement the statistics word for friends
import logging
import stats_word as s
import requests
from pyquery import PyQuery as pq
import yagmail
import wxpy
from wxpy import *
# from mymodule import stats_word

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message: %(message)s',level=logging.DEBUG)

# get the article from the wechat
def get_article(url):
    response = requests.get(url)
    document = pq(response.text)
    content = document('#js_content').text()
    return content

def main():
    bot = Bot() # 
    friends = bot.friends()

    @bot.register(friends, SHARING)
    def handler(msg):
        try:
            logging.info('sharing url - %s', msg.url)
            article = get_article(msg.url)
            result = s.stats_text_cn(article)[0]
            msg.reply(str(result))
        except Exception as e:
            logging.exception(e)
    embed()

if __name__ == "__main__":
    main()

