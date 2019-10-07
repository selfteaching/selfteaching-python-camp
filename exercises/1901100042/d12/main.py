import getpass
import yagmail
import stats_word
import logging
import requests
import pyquery
from wxpy import *

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)

#提取文章正文
def get_article(url):
    words = requests.get(url)
    document = pyquery.PyQuery(words.text)
    return document('#js_content').text()

def main():
    bot = Bot()
    friends = bot.friends()

    @bot.register(friends,SHARING)
    def handler(msg):
        try:
            article = get_article(msg.url)
            result = stats_word.stats_text_cn(article,100)
            logging.info('sharing url =%s',msg.url)
            msg.reply(str(result))
        except Exception as e:
            logging.exception(e)
    embed()

if __name__ == '__main__':
    main()
