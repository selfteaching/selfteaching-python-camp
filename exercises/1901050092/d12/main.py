import logging
import requests
import pyquery
from wxpy import *
from mymodule import stats_word

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|massage: %(massage)s',level=logging.DEBUG)

def get_article(url):
    r = requests.get(url)
    document = pyquery.PyQuery(r.text)
    return document('#js_counter').text()


def mian():
    bot = Bot()
    FRIENDS = bot.friends()

    @bot.register(FRIENDS,SHARING)
    def handler(msg):
        try:
            logging.info('sharing url = %s',msg.url)
            article = get_article(msg.url)
            result = stats_word.stats_text_cn(article,100)
            msg.reply(str(result))
        except Exception as e:
            logging.exception(e)
    embed()

if __name__ == "__mian__":
    mian()
